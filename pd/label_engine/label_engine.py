# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Label Engine messages
"""
import math
from dataclasses import dataclass
from enum import IntEnum
from pathlib import Path
import io
from typing import Optional, Tuple

import cv2
import numpy as np
from google.protobuf.json_format import Parse
from io import BytesIO

from pd.core import PdError

from pd.internal.proto.label_engine.generated.python.annotation_pb2 import Annotation
# These imports are needed to allow parsing of proto messages
# We may want to switch these to dynamically import all classes in that directory
from pd.internal.proto.label_engine.generated.python.annotation_pb2 import *
from pd.internal.proto.label_engine.generated.python.agent_state_pb2 import *
from pd.internal.proto.label_engine.generated.python.bounding_box_2d_pb2 import *
from pd.internal.proto.label_engine.generated.python.bounding_box_3d_pb2 import *
from pd.internal.proto.label_engine.generated.python.camera_calibration_pb2 import *
from pd.internal.proto.label_engine.generated.python.geometry_pb2 import *
from pd.internal.proto.label_engine.generated.python.ig_metadata_pb2 import *
from pd.internal.proto.label_engine.generated.python.instance_map_pb2 import *
from pd.internal.proto.label_engine.generated.python.instance_point_pb2 import *
from pd.internal.proto.label_engine.generated.python.mesh_map_pb2 import *
from pd.internal.proto.label_engine.generated.python.motion_vectors_2d_pb2 import *
from pd.internal.proto.label_engine.generated.python.transform_map_pb2 import *
from pd.internal.proto.label_engine.generated.python.umd_data_pb2 import *


_ID_U16_TO_COLOR_LOOKUP = cv2.applyColorMap(
    np.random.randint(0, 256, 65536, dtype=np.uint8), cv2.COLORMAP_JET
).reshape(-1, 3).astype(np.float32)


# TODO: auto generate wrapper class from proto
class DataType(IntEnum):
    NoneType = 0
    Image = 1
    Mesh = 2
    MeshMap = 3
    Null = 4
    TransformMap = 5
    Sensor = 6
    MeshIDMap = 7
    PointCloud = 8
    Annotation = 9
    UMD = 10
    SimState = 11
    CameraDistortionCalibration = 12
    Configuration = 13
    IGMetadata = 14
    Telemetry = 15


@dataclass
class LabelData:
    """
    Label data for a single data object
    """

    timestamp: Optional[str]
    """Timestamp of the data object, if applicable"""

    sensor_id_and_name: Optional[Tuple[int, str]]
    """Agent id and name of the sensor of the data object, if applicable"""

    label: str
    """Name of the data stream"""

    data: bytes
    """Label data"""

    @property
    def data_as_rgb(self) -> np.ndarray:
        """
        Returns data as a 3-channel RGB buffer
        """
        im_bgr = cv2.imdecode(np.frombuffer(io.BytesIO(self.data).read(), np.uint8), cv2.IMREAD_COLOR)
        return cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)

    @property
    def data_as_depth(self) -> np.ndarray:
        """
        Returns data array as a single-channel float32 depth buffer
        """
        with np.load(BytesIO(self.data)) as npz_data:
            data = npz_data['data']
            return data

    @property
    def data_as_segmentation_ids(self) -> np.ndarray:
        """
        Returns data array as a single-channel 2D buffer where each pixel
        maps to its uint16 segmentation id
        """
        im_semseg = cv2.imdecode(np.frombuffer(io.BytesIO(self.data).read(), np.uint8), cv2.IMREAD_UNCHANGED)
        im_semseg = cv2.cvtColor(im_semseg, cv2.COLOR_BGRA2RGBA)
        semseg = im_semseg.view(dtype=np.uint16)[:, :, 0]
        return semseg

    @property
    def data_as_segmentation_rgb(self) -> np.ndarray:
        """
        Returns data array as an RGB segmentation image
        """
        return _ID_U16_TO_COLOR_LOOKUP[self.data_as_segmentation_ids].astype(np.uint8)

    @property
    def data_as_instance_ids(self) -> np.ndarray:
        """
        Returns data array as a single-channel 2D buffer where each pixel
        maps to its uint16 instance id
        """
        im_instance_seg = cv2.imdecode(np.frombuffer(io.BytesIO(self.data).read(), np.uint8), cv2.IMREAD_UNCHANGED)
        im_instance_seg = cv2.cvtColor(im_instance_seg, cv2.COLOR_BGRA2RGBA)
        instance_seg = im_instance_seg.view(dtype=np.uint16)[:, :, 0]
        return instance_seg

    @property
    def data_as_instance_rgb(self) -> np.ndarray:
        """
        Returns data array as an RGB instances image
        """
        return _ID_U16_TO_COLOR_LOOKUP[self.data_as_instance_ids].astype(np.uint8)

    def get_data_as_merged_instance_rgb(self, rgb: np.ndarray) -> np.ndarray:
        """
        Returns data array as an RGB instances image.
        The instance image is merged with a given rgb image

        Args:
            rgb: The rgb image with which to merge the instance image
        """
        instance_image_rgb = self.data_as_instance_rgb.astype(np.float64)
        # Height and width must match, channels can be 3 (color) or 1 (grayscale)
        if rgb.shape[:2] != instance_image_rgb.shape[:2]:
            raise PdError(f"Rgb image size {str(rgb.shape[:2])} must match the instances "
                          f"image size {str(instance_image_rgb.shape[:2])}")
        # Generates instance id alpha mask
        # Alpha mask has a non-zero alpha value for every non-zero pixel in instances rgb image
        # Lastly, broadcasts alpha to match dims of rgb image
        alpha = np.sum(instance_image_rgb, axis=2)
        alpha[alpha > 0] = 0.5
        alpha = np.expand_dims(alpha, axis=2)
        alpha = np.broadcast_to(alpha, shape=instance_image_rgb.shape)
        # Generates output image by combining rgb image with instances image
        output_img = rgb * (1-alpha) + instance_image_rgb * alpha
        return output_img.astype(np.uint8)

    @property
    def data_as_surface_normals(self) -> np.ndarray:
        """
        Returns data array as a buffer containing surface normal vectors

        Returned buffer is a numpy.float64 matrix of shape `(H X W x 3)`, where `H` is the height and `W` is the width
        of corresponding camera image. The third axis contains the x, y and z normal direction of the surface sampled
        by the pixel in the camera coordinate system.
        """
        im_normals = cv2.imdecode(np.frombuffer(io.BytesIO(self.data).read(), np.uint8), cv2.IMREAD_COLOR)
        im_normals = cv2.cvtColor(im_normals, cv2.COLOR_BGR2RGB)
        quantized_norms = im_normals
        quantized_norms_f = quantized_norms.astype(np.float64)
        dequantized_norms_f = ((quantized_norms_f / 255) - 0.5) * 2
        dequantized_norms_f = dequantized_norms_f / np.linalg.norm(dequantized_norms_f, axis=-1, keepdims=True)
        return dequantized_norms_f

    @property
    def data_as_annotation(self) -> Annotation:
        """
        Parses data as an Annotation Data Object

        Returns:
            Annotation data object proto message
        """
        json_s = self.data.decode()
        message: Annotation = Parse(json_s, Annotation())
        return message


def load_pipeline_config(name: str) -> str:
    """
    Load one of the provided default pipeline configs for Label Engine

    Args:
        name: Name of the config

    Returns:
        Config as a string
    """
    import pd.internal.label_engine_configs as label_engine_configs
    base_configs_path = Path(label_engine_configs.__file__).resolve().parent
    config_path = base_configs_path / f"{name}.pb.json"
    if not config_path.exists():
        raise PdError(f"Couldn't find Label Engine pipeline config named '{name}'.")
    with config_path.open('r') as f:
        config_data = f.read()
    return config_data


def simulation_time_as_timestamp(simulation_time_sec: float) -> str:
    """
    Convert simulation time from :class:`pd.state.State` into a timestamp for
    Label Engine

    Args:
        simulation_time_sec: Simulation time

    Returns:
        Timestamp for Label Engine
    """
    return f"{int(math.ceil(simulation_time_sec*1000.0)):09d}"
