import math

import numpy as np
from pyquaternion import Quaternion

from pd.state.pose6d import Pose6D


class TestPose6D:
    def test_default_instance(self):
        pose = Pose6D()
        assert pose.translation == (0., 0., 0.)
        assert pose.rotation == Quaternion()

    def test_translation_to_matrix(self):
        pose = Pose6D.from_translation(
            x_metres=1.0, y_metres=-2.0, z_metres=3.0
        )
        result = pose.as_transformation_matrix()
        expected = np.array([
            [1.0, 0.0, 0.0, 1.0],
            [0.0, 1.0, 0.0, -2.0],
            [0.0, 0.0, 1.0, 3.0],
            [0.0, 0.0, 0.0, 1.0],
        ], dtype=np.float32)
        assert np.allclose(result, expected)

    def test_euler_to_matrix(self):
        # Test data generated as follows:
        # https://www.mecademic.com/en/how-is-orientation-in-space-represented-with-euler-angles
        # Order: XYZ extrinsic = Z'Y'X'
        # Angles: ignore angle names on website, use X'=alpha, Y'=beta, Z'=gamma
        pose = Pose6D.from_euler_angles(
            x_metres=1.0, y_metres=2.0, z_metres=3.0,
            alpha_radians=math.pi/2, beta_radians=math.pi/2, gamma_radians=0
        )
        result = pose.as_transformation_matrix()
        expected = np.array([
            [0.0, 1.0, 0.0, 1.0],
            [0.0, 0.0, -1.0, 2.0],
            [-1.0, 0.0, 0.0, 3.0],
            [0.0, 0.0, 0.0, 1.0],
        ], dtype=np.float32)
        assert np.allclose(result, expected)

        pose = Pose6D.from_euler_angles(
            x_metres=1.0, y_metres=2.0, z_metres=3.0,
            alpha_radians=0, beta_radians=math.pi/2, gamma_radians=math.pi/2
        )
        result = pose.as_transformation_matrix()
        expected = np.array([
            [0.0, -1.0, 0.0, 1.0],
            [0.0, 0.0, 1.0, 2.0],
            [-1.0, 0.0, 0.0, 3.0],
            [0.0, 0.0, 0.0, 1.0],
        ], dtype=np.float32)
        assert np.allclose(result, expected)

        pose = Pose6D.from_euler_angles(
            x_metres=1.0, y_metres=2.0, z_metres=3.0,
            alpha_radians=math.pi/2, beta_radians=0, gamma_radians=math.pi/2
        )
        result = pose.as_transformation_matrix()
        expected = np.array([
            [0.0, 0.0, 1.0, 1.0],
            [1.0, 0.0, 0.0, 2.0],
            [0.0, 1.0, 0.0, 3.0],
            [0.0, 0.0, 0.0, 1.0],
        ], dtype=np.float32)
        assert np.allclose(result, expected)

        pose = Pose6D.from_euler_angles(
            x_metres=1.0, y_metres=2.0, z_metres=3.0,
            alpha_radians=math.pi/4, beta_radians=math.pi/4, gamma_radians=math.pi/4
        )
        result = pose.as_transformation_matrix()
        expected = np.array([
            [0.5, -0.1464466, 0.8535534, 1.0],
            [0.5000000, 0.8535534, -0.1464466, 2.0],
            [-0.7071068, 0.5, 0.5, 3.0],
            [0.0, 0.0, 0.0, 1.0],
        ], dtype=np.float32)
        assert np.allclose(result, expected)

    def test_rpy_to_matrix(self):
        # Test data generated as follows:
        # https://www.mecademic.com/en/how-is-orientation-in-space-represented-with-euler-angles
        # Order: RPY extrinsic = YPR intrinsic = Z'X'Y'
        # Angles: R=Y'=gamma, P=X'=beta, Y=Z'=alpha
        pose = Pose6D.from_rpy_angles(
            x_metres=1.0, y_metres=2.0, z_metres=3.0,
            roll_degrees=90, pitch_degrees=90, yaw_degrees=0
        )
        result = pose.as_transformation_matrix()
        expected = np.array([
            [0.0, 0.0, 1.0, 1.0],
            [1.0, 0.0, 0.0, 2.0],
            [0.0, 1.0, 0.0, 3.0],
            [0.0, 0.0, 0.0, 1.0],
        ], dtype=np.float32)
        assert np.allclose(result, expected)

        pose = Pose6D.from_rpy_angles(
            x_metres=1.0, y_metres=2.0, z_metres=3.0,
            roll_degrees=0, pitch_degrees=90, yaw_degrees=90
        )
        result = pose.as_transformation_matrix()
        expected = np.array([
            [0.0, 0.0, 1.0, 1.0],
            [1.0, 0.0, 0.0, 2.0],
            [0.0, 1.0, 0.0, 3.0],
            [0.0, 0.0, 0.0, 1.0],
        ], dtype=np.float32)
        assert np.allclose(result, expected)

        pose = Pose6D.from_rpy_angles(
            x_metres=1.0, y_metres=2.0, z_metres=3.0,
            roll_degrees=90, pitch_degrees=0, yaw_degrees=90
        )
        result = pose.as_transformation_matrix()
        expected = np.array([
            [0.0, -1.0, 0.0, 1.0],
            [0.0, 0.0, 1.0, 2.0],
            [-1.0, 0.0, 0.0, 3.0],
            [0.0, 0.0, 0.0, 1.0],
        ], dtype=np.float32)
        assert np.allclose(result, expected)

        pose = Pose6D.from_rpy_angles(
            x_metres=1.0, y_metres=2.0, z_metres=3.0,
            roll_degrees=45, pitch_degrees=45, yaw_degrees=45
        )
        result = pose.as_transformation_matrix()
        expected = np.array([
            [0.1464466, -0.5, 0.8535534, 1.0],
            [0.8535534, 0.5, 0.1464466, 2.0],
            [-0.5, 0.7071068, 0.5, 3.0],
            [0.0, 0.0, 0.0, 1.0],
        ], dtype=np.float32)
        assert np.allclose(result, expected)

    def test_matrix_to_matrix(self):
        pose = Pose6D.from_transformation_matrix(
            matrix=np.array([
                [0.5, -0.1464466, 0.8535534, 1.0],
                [0.5000000, 0.8535534, -0.1464466, 2.0],
                [-0.7071068, 0.5, 0.5, 3.0],
                [0.0, 0.0, 0.0, 1.0],
            ], dtype=np.float32)
        )
        result = pose.as_transformation_matrix()
        expected = np.array([
            [0.5, -0.1464466, 0.8535534, 1.0],
            [0.5000000, 0.8535534, -0.1464466, 2.0],
            [-0.7071068, 0.5, 0.5, 3.0],
            [0.0, 0.0, 0.0, 1.0],
        ], dtype=np.float32)
        assert np.allclose(result, expected)

    def test_multiply(self):
        pose1 = Pose6D.from_rpy_angles(
            x_metres=0.0, y_metres=0.0, z_metres=0.0,
            roll_degrees=0.0, pitch_degrees=0.0, yaw_degrees=15.0
        )
        pose2 = Pose6D.from_rpy_angles(
            x_metres=0.0, y_metres=0.0, z_metres=0.0,
            roll_degrees=0.0, pitch_degrees=45.0, yaw_degrees=0.0
        )
        result_pose = pose1 * pose2
        expected_pose = Pose6D.from_rpy_angles(
            x_metres=0.0, y_metres=0.0, z_metres=0.0,
            roll_degrees=0.0, pitch_degrees=45.0, yaw_degrees=15.0
        )
        result = result_pose.as_transformation_matrix()
        expected = expected_pose.as_transformation_matrix()
        assert np.allclose(result, expected)
