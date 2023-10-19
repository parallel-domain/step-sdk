# Copyright (c) 2022 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Utility function to help generate snapshot images of assets
"""

import logging
import math
from pprint import PrettyPrinter
from typing import Callable, List, Tuple

import numpy as np

from pd.assets import ObjAssets, asset_coords_to_sim_coords, get_vehicle_wheel_names, get_vehicle_wheel_poses
from pd.session import SimSession
from pd.sim import Raycast, RaycastHit
from pd.state import (
    CameraSensor,
    DistortionParams,
    ModelAgent,
    Pose6D,
    PostProcessParams,
    SensorAgent,
    State,
    VehicleAgent,
    WorldInfo,
)

logger = logging.getLogger(__name__)
pp = PrettyPrinter()


_LOCATION = "FICT_Racetrack_1000_1"
_TIME_OF_DAY = "day_clear_06"

# These coordinates are hand-picked for the chosen _LOCATION

_ASSET_OFFSET = (471.7, 1.81, 0)


def get_asset_rotated_bbox(asset_obj: ObjAssets, pose: Pose6D) -> List[Tuple[float, float, float]]:
    """
    Get the bounding box of an Asset after it has been rotated by the rotation specified
    in the Pose

    Args:
        asset_obj: The asset object
        pose: The rotation. Note that translation in this pose is ignored

    Returns:
        Rotated bounded box as a list of 8 vertices
    """
    bbox_leaves = (
        asset_obj.bbox_min_leaves_x,
        asset_obj.bbox_min_leaves_y,
        asset_obj.bbox_min_leaves_z,
        asset_obj.bbox_max_leaves_x,
        asset_obj.bbox_max_leaves_y,
        asset_obj.bbox_max_leaves_z,
    )
    bbox_corners = (
        asset_obj.bbox_min_x,
        asset_obj.bbox_min_y,
        asset_obj.bbox_min_z,
        asset_obj.bbox_max_x,
        asset_obj.bbox_max_y,
        asset_obj.bbox_max_z,
    )

    # trees have separate boxes for their trunk and canopy, find the largest dimensions to get the full tree in frame
    if None not in bbox_leaves and 0 not in bbox_leaves:
        (minx, miny, minz, maxx, maxy, maxz) = (
            min(asset_obj.bbox_min_x, asset_obj.bbox_min_leaves_x),
            min(asset_obj.bbox_min_y, asset_obj.bbox_min_leaves_y),
            min(asset_obj.bbox_min_z, asset_obj.bbox_min_leaves_z),
            max(asset_obj.bbox_max_x, asset_obj.bbox_max_leaves_x),
            max(asset_obj.bbox_max_y, asset_obj.bbox_max_leaves_y),
            max(asset_obj.bbox_max_z, asset_obj.bbox_max_leaves_z),
        )
    else:
        (minx, miny, minz, maxx, maxy, maxz) = bbox_corners

    if all(corner == 0 or corner is None for corner in bbox_corners):
        logger.warning(f"{asset_obj.name} is missing bounding box data - may not visualize")
        # Missing data in asset registry, choose defaults
        (minx, miny, minz, maxx, maxy, maxz) = (-0.6, 0.0, -0.5, 0.6, 1.0, 0.5)

    vertices = [
        (minx, miny, minz),
        (minx, miny, maxz),
        (minx, maxy, minz),
        (minx, maxy, maxz),
        (maxx, miny, minz),
        (maxx, miny, maxz),
        (maxx, maxy, minz),
        (maxx, maxy, maxz),
    ]
    # convert from asset bbox coordinate frame to sim coordinate frame
    vertices = [asset_coords_to_sim_coords(x, y, z) for x, y, z in vertices]
    rotation_matrix = pose.as_transformation_matrix()[:3, :3]
    rotated_vertices = [tuple(np.matmul(rotation_matrix, np.array(v))) for v in vertices]
    logger.debug(f"{asset_obj.name} vertices\n{pp.pformat(vertices)}")
    logger.debug(f"{asset_obj.name} rotated_vertices\n{pp.pformat(rotated_vertices)}")
    return rotated_vertices


def generate_camera_pose_for_rotated_bbox(
    rotated_bbox: List[Tuple[float, float, float]], sensor: CameraSensor, adjusted_origin
) -> Pose6D:
    """
    Given the rotated bbox for an asset, generate the pose for a :class:`~pd.state.CameraSensor`
    such that the asset has good framing and zoom level.

    This is done by selecting a camera displacement in the Y-axis such that the asset fits within
    the frame. The resulting camera pose is guaranteed to have zero rotation - i.e. it will be
    facing the +Y direction.

    Args:
        rotated_bbox: Rotated bbox for the asset
        sensor: Camera sensor
        adjusted_origin: Apply a translation to camera sensor pose

    Returns:
        Pose for the camera sensor
    """
    # Let's start by figuring out which axis will be used to determine the camera displacement/zoom level
    # Our options are:
    #   * Image axis u (i.e. world axis x)
    #   * Image axis v (i.e. world axis z)
    # We do this by computing an axis aligned bbox and picking the dimension with the larger size
    # Note: we assume a square sensor image, this comparison needs to be scaled for a rectangular image
    aa_bbox = [
        (min(x for x, y, z in rotated_bbox), min(z for x, y, z in rotated_bbox)),
        (max(x for x, y, z in rotated_bbox), max(z for x, y, z in rotated_bbox)),
    ]
    width = aa_bbox[1][0] - aa_bbox[0][0]
    height = aa_bbox[1][1] - aa_bbox[0][1]
    logger.debug(f"width {width}, height {height}")
    # TODO: determining the min, max vertices is not perfect, do a test
    #       projection to determine the extremes
    if width > height:
        # pick the two vertices at either ends along world x-axis
        v_min = min(rotated_bbox, key=lambda a: a[0])
        v_max = max(rotated_bbox, key=lambda a: a[0])
        # Check if there are multiple vertices with same extreme x-values
        # Pick the one closest to camera (min y-value) as extremes used for scaling
        x_min, x_max = v_min[0], v_max[0]
        v_min = min([a for a in rotated_bbox if np.isclose(a[0], x_min)], key=lambda a: a[1])
        v_max = min([a for a in rotated_bbox if np.isclose(a[0], x_max)], key=lambda a: a[1])
    else:
        # pick the two vertices at either ends along world z-axis
        v_min = min(rotated_bbox, key=lambda a: a[2])
        v_max = max(rotated_bbox, key=lambda a: a[2])
        # Check if there are multiple vertices with same extreme z-values
        # Pick the one closest to camera (min y-value) as extremes used for scaling
        z_min, z_max = v_min[2], v_max[2]
        v_min = min([a for a in rotated_bbox if np.isclose(a[2], z_min)], key=lambda a: a[1])
        v_max = min([a for a in rotated_bbox if np.isclose(a[2], z_max)], key=lambda a: a[1])
    logger.debug(f"v_min, v_max {v_min, v_max}")

    # Now we determine the translation of the camera sensor
    # The model is as follows
    # We are given:
    #   * Camera intrinsics: fx, fy, cx, cy, width, height
    #   * Two vertices at extreme ends of the axis
    #   * Padding ratio
    # We want to find the camera translation (tx, ty, tz) such that
    # resulting image spans across these two vertices with some
    # padding at either ends.
    # To do this we expand the camera projection matrix and solve for
    # either (tx, ty) or (tz, ty) depending on which axis we're
    # scaling against. For the remaining t-parameter we will simply
    # pick the center
    # The linear equations we solve are:
    #   fx*tx + (cx-u1)*ty = fx*x1 + (cx-u1)*y1
    #   fx*tx + (cx-u2)*ty = fx*x2 + (cx-u2)*y2
    # Where:
    #   (x1,y1) and (x2,y2) are two extreme vertices in world coordinates
    #   u1, u2 are pixel coordinate where extreme vertices should be projected after padding
    # Replace x1,x2->z1,z2 and fx,cx->fy,cy if scaling along the world z-axis
    padding = 0.2
    if width > height:
        fa, ca = sensor.distortion_params.fx, sensor.distortion_params.cx
        a1, a2 = v_min[0], v_max[0]
        y1, y2 = v_min[1], v_max[1]
        u1, u2 = padding * sensor.width, (1.0 - padding) * sensor.width
    else:
        fa, ca = sensor.distortion_params.fy, sensor.distortion_params.cy
        a1, a2 = v_min[2], v_max[2]
        y1, y2 = v_min[1], v_max[1]
        u1, u2 = padding * sensor.height, (1.0 - padding) * sensor.height
    # Solve As = B for s, which will contain (ta, ty) where a=x-axis or z-axis
    A = np.array([[fa, ca - u1], [fa, ca - u2]])
    B = np.array([fa * a1 + (ca - u1) * y1, fa * a2 + (ca - u2) * y2])
    s = np.linalg.solve(A, B)
    ty = s[1]
    if width > height:
        tx = s[0]
        z_min = min(rotated_bbox, key=lambda a: a[2])
        z_max = max(rotated_bbox, key=lambda a: a[2])
        tz = (z_min[2] + z_max[2]) / 2.0
    else:
        tz = s[0]
        x_min = min(rotated_bbox, key=lambda a: a[0])
        x_max = max(rotated_bbox, key=lambda a: a[0])
        tx = (x_min[0] + x_max[0]) / 2.0
    logger.debug(f"s {s} | tx, ty, tz {tx, ty, tz}")

    camera_x_offset, camera_y_offset, camera_z_offset = adjusted_origin
    sensor_pose = Pose6D.from_rpy_angles(
        x_metres=tx + camera_x_offset,
        y_metres=ty + camera_y_offset,
        z_metres=tz + camera_z_offset,
        roll_degrees=0.0,
        pitch_degrees=0.0,
        yaw_degrees=0.0,
    )
    logger.debug(f"sensor translation {sensor_pose.translation}")
    return sensor_pose


def generate_state_for_asset_snap(
    asset_obj: ObjAssets, resolution: Tuple[int, int], raycast: Callable[[List[Raycast]], List[List[RaycastHit]]]
) -> State:
    """
    Generate the complete :class:`pd.state.State` for snapping a picture of an asset.

    The State contains one SensorAgent with a CameraSensor attached, and one Model or Vehicle agent
    depending on the type of asset. The asset is first rotated into a favourable position for
    a picture. Then the CameraSensor is positioned so that the asset is centered and covers most of
    the frame.

    Args:
        asset_obj: The asset of which to snap a picture
        resolution: Image resolution (width, height)
        raycast: Active SimSession raycast method

    Returns:
        Complete State needed to generate the picture of the asset
    """
    image_width, image_height = resolution
    category_name = (
        asset_obj.asset_category.name if asset_obj.asset_category and asset_obj.asset_category.name else "none"
    )

    # Placement of asset on the map
    asset_x_offset, asset_y_offset, asset_z_offset = _ASSET_OFFSET

    if category_name == "vehicle":
        agent_pose = Pose6D.from_rpy_angles(
            x_metres=asset_x_offset,
            y_metres=asset_y_offset,
            z_metres=asset_z_offset,
            roll_degrees=0.0,
            pitch_degrees=0.0,
            yaw_degrees=120.0,
        )
    else:
        asset_z_offset += abs(asset_obj.bbox_min_y)
        agent_pose = Pose6D.from_rpy_angles(
            x_metres=asset_x_offset,
            y_metres=asset_y_offset,
            z_metres=asset_z_offset,
            roll_degrees=0.0,
            pitch_degrees=0.0,
            yaw_degrees=160,
        )

    rotated_bbox = get_asset_rotated_bbox(asset_obj, agent_pose)
    target_fov_degrees = 35.0
    fx = image_width / (2.0 * math.tan(math.radians(target_fov_degrees / 2.0)))
    fy = image_height / (2.0 * math.tan(math.radians(target_fov_degrees / 2.0)))
    camera_sensor = CameraSensor(
        name="Front",
        pose=Pose6D.from_rpy_angles(
            x_metres=0.0, y_metres=0.0, z_metres=0.0, roll_degrees=0.0, pitch_degrees=0.0, yaw_degrees=0.0
        ),
        width=image_width,
        height=image_height,
        distortion_params=DistortionParams(
            fx=fx,
            fy=fy,
            cx=image_width * 0.5,
            cy=image_height * 0.5,
        ),
        post_process_params=PostProcessParams(),
        capture_rgb=True,
    )
    camera_pose = generate_camera_pose_for_rotated_bbox(
        rotated_bbox=rotated_bbox,
        sensor=camera_sensor,
        adjusted_origin=(asset_x_offset, asset_y_offset, asset_z_offset),
    )

    # check if camera is under terrain using raycast
    camera_pose_raycast = Raycast(
        origin=(camera_pose.translation[0], camera_pose.translation[1], 1000), direction=(0, 0, -1), max_distance=5000
    )

    raycast_response = raycast([camera_pose_raycast])
    if len(raycast_response[0]) == 1:
        if camera_pose.translation[2] < raycast_response[0][0].position[2] + 0.2:
            # move camera slightly up and backwards
            camera_pose.translation = (
                camera_pose.translation[0],
                camera_pose.translation[1] - 0.2,
                raycast_response[0][0].position[2] + 0.1,
            )

    # Adjust dof focal distance based on camera position (is in cms)
    distance_to_agent = agent_pose.translation[1] - camera_pose.translation[1]
    camera_sensor.post_process_params.dof_focal_distance = 100.0 * distance_to_agent
    camera_sensor.post_process_params.dof_depth_blur_amount = 0.01
    sensor_agent = SensorAgent(id=1, pose=camera_pose, velocity=(0.0, 0.0, 0.0), sensors=[camera_sensor])

    vehicle_agent = VehicleAgent(
        id=3,
        pose=Pose6D.from_translation(x_metres=0.0, y_metres=-100.0, z_metres=0.0),
        velocity=(0, 0, 0),
        vehicle_type="",
    )
    model_agent = ModelAgent(
        id=2,
        pose=Pose6D.from_translation(x_metres=0.0, y_metres=-100.0, z_metres=0.0),
        velocity=(0.0, 0.0, 0.0),
        asset_name="",
    )

    agent_to_show = []
    if category_name == "vehicle":
        vehicle_name = asset_obj.name
        vehicle_wheels = get_vehicle_wheel_names(vehicle_name)
        wheel_name = vehicle_wheels[0] if vehicle_wheels else None
        wheel_poses = get_vehicle_wheel_poses(vehicle_name, wheel_name) if vehicle_wheels else []
        vehicle_agent.pose = agent_pose
        vehicle_agent.vehicle_type = vehicle_name
        vehicle_agent.wheel_type = wheel_name
        vehicle_agent.wheel_poses = wheel_poses
        vehicle_agent.lock_to_ground = True
        agent_to_show.append(vehicle_agent)
    else:
        model_agent.pose = agent_pose
        model_agent.asset_name = asset_obj.name
        model_agent.lock_to_ground = False
        agent_to_show.append(model_agent)

    world_info = WorldInfo(location=_LOCATION, time_of_day=_TIME_OF_DAY)

    state = State(simulation_time_sec=0, world_info=world_info, agents=[sensor_agent, *agent_to_show])  # fill in later
    return state


def get_location_for_asset_snap() -> str:
    """
    Returns the location used for asset snaphosts

    Returns:
        Location name
    """
    return _LOCATION
