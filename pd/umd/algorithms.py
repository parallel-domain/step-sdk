# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Algorithms for reading and traversing UMD data
"""

from typing import List, Generator, Tuple, Callable
import math
from itertools import chain

import numpy as np
from shapely.geometry import LineString

import pd.state
import pd.internal.umd.UMD_pb2 as schema


LaneSegmentTraversalStrategy = Callable[
    [schema.LaneSegment, List[schema.LaneSegment]],
    schema.LaneSegment
]
"""
Callable that defines strategy for selecting next lane segment.

Args:
    LaneSegment: The previous lane segment
    List[LaneSegment]: Candidates for next lane segment

Returns:
    The next lane segment
"""


def traverse_lane_segments(umd_map: schema.UniversalMap,
                           start_lane_segment_id: int,
                           traversal_strategy: LaneSegmentTraversalStrategy) \
        -> Generator[schema.LaneSegment, None, None]:
    """
    Traverse lane segments by providing a strategy to select next lane

    This is a generator that traverses lane segments by using the provided strategy. The strategy is a callable that
    takes as input a list of successor lane segments and returns the next lane segment to traverse.

    Example:

        This example selects a random successor lane segment with every iteration::

            traverse_lane_segments(
                umd_map=umd_map,
                start_lane_segment_id=0,
                traversal_strategy=lambda previous, successors: random.choice(successors)
            )
            first_segment = next(traverse_lane_segments)
            second_segment = next(traverse_lane_segments)

    Args:
        umd_map: The UMD map
        start_lane_segment_id: Id of the starting lane segment
        traversal_strategy: Callable defining the traversal strategy

    Returns:
        A generator that generates lane segments as they are traversed
    """
    lane_segment = umd_map.lane_segments.get(start_lane_segment_id)
    yield lane_segment
    while lane_segment.successors:
        lane_segment = traversal_strategy(
            lane_segment,
            [umd_map.lane_segments.get(lane_id) for lane_id in lane_segment.successors]
        )
        yield lane_segment


def move_along_path(path_points: List[Tuple[float, float, float]],
                    start_offset_metres: float) -> Generator[pd.state.Pose6D, float, None]:
    """
    Generate Poses along a specified path

    This is a generator that returns Poses along a path. The Poses are oriented to point in the direction
    of the path. Each iteration of the generator should be called with `send(distance)` where `distance`
    is the amount of displacement between the previous position and next position.

    Example:
        To use the generator  1) instantiate by calling this method, 2) call `next()` to retrieve the starting pose,
        3) call `send(distance)` for subsequent poses::

            poses = move_along_path(
                path_points=path_points,
                start_offset_metres=0.0,
            )
            first_pose = next(poses)
            second_pose = poses.send(2.0)
            third_pose = poses.send(2.0)

    Args:
        path_points: The path as a list of points (3-tuple)
        start_offset_metres: Distance offset for the starting Pose

    Returns:
        A generator that generates Poses
    """
    def generate_pose(curr_pos, fut_pos):
        c = np.array(curr_pos)
        f = np.array(fut_pos)
        forward = (f-c) / np.linalg.norm(f-c)
        pose = pd.state.Pose6D.from_direction(
            x_metres=current_pos[0], y_metres=current_pos[1], z_metres=current_pos[2],
            direction=tuple(forward)
        )
        return pose

    path = LineString(path_points)
    distance = start_offset_metres
    current_pos = path.interpolate(distance).coords[0]
    future_pos = path.interpolate(distance+1.0).coords[0]
    while distance < path.length:
        distance_step = yield generate_pose(current_pos, future_pos)
        distance += distance_step
        current_pos = path.interpolate(distance).coords[0]
        future_pos = path.interpolate(distance+distance_step).coords[0]


def get_edge_length_in_metres(edge: schema.Edge) -> float:
    """
    Returns the total length of the Edge line object in a Umd map

    Args:
        edge: Edge object in a Umd map

    Returns:
        Length of the Edge
    """
    return LineString([(p.x, p.y, p.z) for p in edge.points]).length


def get_nearest_point_to(umd_map: schema.UniversalMap, x: float, y: float) -> Tuple[float, float, float]:
    """
    Returns the point in Umd map closest to the given x,y coordinate.

    Args:
        x: X-coordinate
        y: Y-coordinate

    Returns:
        (x, y, z) coordinates of the closest point
    """
    nearest_point = min(
        chain.from_iterable(e.points for e in umd_map.edges.values()),
        key=lambda p: math.dist((p.x, p.y), (x, y))
    )
    return nearest_point.x, nearest_point.y, nearest_point.z
