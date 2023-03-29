# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
6D pose representation

See class :class:`Pose6D` for details.
"""


from dataclasses import dataclass, field
from typing import Tuple

import numpy as np
from pyquaternion import Quaternion


@dataclass
class Pose6D:
    """
    Represents a 6D pose

    The 6D pose consists of a 3D rotation followed by a 3D translation.
    The pose is always relative to another coordinate system.
    For example, the pose for an agent is relative to the world coordinate system,
    while the sensor pose is relative to the agent's coordinate system.

    Our world coordinate system is east, north, up (ENU).
         * Positive X-axis is east
         * Positive Y-axis is north
         * Positive Z-axis is up

    Our agent coordinate system is Right-Forward-Up (RFU).
        * X-axis points to the right-hand side of the vehicle or agent. It is also the Pitch axis.
        * Y-axis points to the front of the vehicle or agent. It is also the Roll axis.
        * Z-axis points up through the roof of the vehicle or agent. It is also the Yaw axis.
        * See `this article <https://en.wikipedia.org/wiki/Aircraft_principal_axes>`_ for reference.
    """
    rotation: Quaternion = field(default_factory=Quaternion)
    translation: Tuple[float, float, float] = field(default_factory=lambda: (0, 0, 0))

    @classmethod
    def from_translation(
            cls,
            x_metres: float, y_metres: float, z_metres: float
    ) -> "Pose6D":
        """
        Constructs a :class:`Pose6D` object from translation only

        Args:
            x_metres: Translation in X in metres
            y_metres: Translation in Y in metres
            z_metres: Translation in Z in metres

        Returns:
            Pose representation as :class:`Pose6D`
        """
        translation = (x_metres, y_metres, z_metres)
        return cls(translation=translation)

    @classmethod
    def from_direction(
            cls,
            x_metres: float, y_metres: float, z_metres: float,
            direction: Tuple[float, float, float]
    ) -> "Pose6D":
        """
        Constructs a :class:`Pose6D` object from translation and direction vector


        Rotation occurs in two steps using Azimuth-Elevation orientation.
        First rotation occurs along azimuth angle in the xy-plane.
        Second rotation occurs along the elevation angle.
        Second rotation

        Args:
            x_metres: Translation in X in metres
            y_metres: Translation in Y in metres
            z_metres: Translation in Z in metres
            direction: Vector representing direction. Must have at least one non-zero component

        Returns:
            Pose representation as :class:`Pose6D`
        """
        if not any(direction):
            raise ValueError("Direction vector must be non-zero")
        translation = (x_metres, y_metres, z_metres)
        dir_xy_norm = np.array(direction[:2]) / np.linalg.norm(direction[:2])
        rotation_xy = Quaternion(
            axis=(0.0, 0.0, 1.0),
            radians=-np.sign(dir_xy_norm[0])*np.arccos(dir_xy_norm[1])
        )
        theta = np.arcsin(direction[2] / np.linalg.norm(direction))
        rotation_elevation = Quaternion(axis=(dir_xy_norm[1], -dir_xy_norm[0], 0), radians=theta)
        return cls(translation=translation, rotation=rotation_elevation*rotation_xy)

    @classmethod
    def from_euler_angles(
            cls,
            x_metres: float, y_metres: float, z_metres: float,
            alpha_radians: float, beta_radians: float, gamma_radians: float
    ) -> "Pose6D":
        """
        Constructs a :class:`Pose6D` object from translation and rotation vector

        Rotation is represented in Euler XYZ convention in the extrinsic frame.
        Meaning, alpha rotation in X, then beta rotation in Y, then gamma rotation
        in Z.

        Args:
            x_metres: Translation in X in metres
            y_metres: Translation in Y in metres
            z_metres: Translation in Z in metres
            alpha_radians: Rotation in X in radians
            beta_radians: Rotation in Y in radians
            gamma_radians: Rotation in Z in radians

        Returns:
            Pose representation as :class:`Pose6D`
        """
        rotation = Quaternion(axis=(0.0, 0.0, 1.0), radians=gamma_radians) * \
            Quaternion(axis=(0.0, 1.0, 0.0), radians=beta_radians) * \
            Quaternion(axis=(1.0, 0.0, 0.0), radians=alpha_radians)
        translation = (x_metres, y_metres, z_metres)
        return cls(rotation=rotation, translation=translation)

    @classmethod
    def from_rpy_angles(
            cls,
            x_metres: float, y_metres: float, z_metres: float,
            roll_degrees: float, pitch_degrees: float, yaw_degrees: float,
    ) -> "Pose6D":
        """
        Constructs a :class:`Pose6D` object from translation and rotation vector

        Rotation is represented as Roll then Pitch then Yaw (YXZ) in the extrinsic frame.

        Args:
            x_metres: Translation in X in metres
            y_metres: Translation in Y in metres
            z_metres: Translation in Z in metres
            roll_degrees: Rotation in roll axis in degrees
            pitch_degrees: Rotation in pitch axis in degrees
            yaw_degrees: Rotation in yaw axis in degrees

        Returns:
            Pose representation as :class:`Pose6D`
        """
        rotation = Quaternion(axis=(0.0, 0.0, 1.0), degrees=yaw_degrees) * \
            Quaternion(axis=(1.0, 0.0, 0.0), degrees=pitch_degrees) * \
            Quaternion(axis=(0.0, 1.0, 0.0), degrees=roll_degrees)

        translation = (x_metres, y_metres, z_metres)
        return cls(rotation=rotation, translation=translation)

    @classmethod
    def from_transformation_matrix(cls, matrix: np.array) -> "Pose6D":
        """
        Constructs a :class:`Pose6D` object from a transformation matrix representation

        Args:
            matrix: 4x4 transformation matrix

        Returns:
            Pose representation as :class:`Pose6D`
        """
        rotation = Quaternion(matrix=matrix)
        translation = tuple(matrix[:3, 3])
        return cls(rotation=rotation, translation=translation)

    def as_transformation_matrix(self) -> np.array:
        """
        Returns the equivalent 4x4 transformation matrix representation of a :class:`Pose6D`

        Returns:
            4x4 transformation matrix
        """
        matrix = self.rotation.transformation_matrix
        matrix[:3, 3] = np.array(self.translation)
        return matrix

    def __mul__(self, other):
        if not isinstance(other, Pose6D):
            raise TypeError(f"Cannot multiple a Pose6D with {type(other).__name__}")
        return Pose6D.from_transformation_matrix(
            np.matmul(self.as_transformation_matrix(), other.as_transformation_matrix())
        )
