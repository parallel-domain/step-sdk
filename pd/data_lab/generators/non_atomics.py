# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

from pd.internal.proto.keystone.generated.python import pd_spawn_pb2 as pd_spawn_pb2_base
from pd.internal.proto.keystone.generated.wrapper import pd_spawn_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import register_wrapper

from pd.data_lab.generators import BaseGenerator


class NonAtomicGeneratorMessage(BaseGenerator):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.AllVehicleTestScenarioGeneratorInfo)
class AllVehicleTestScenarioGeneratorInfo(pd_spawn_pb2.AllVehicleTestScenarioGeneratorInfo, NonAtomicGeneratorMessage):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.CurveScenarioGeneratorInfo)
class CurveScenarioGeneratorInfo(pd_spawn_pb2.CurveScenarioGeneratorInfo, NonAtomicGeneratorMessage):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.DebrisScenarioGeneratorInfo)
class DebrisScenarioGeneratorInfo(pd_spawn_pb2.DebrisScenarioGeneratorInfo, NonAtomicGeneratorMessage):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.DrivewayScenarioGeneratorInfo)
class DrivewayScenarioGeneratorInfo(pd_spawn_pb2.DrivewayScenarioGeneratorInfo, NonAtomicGeneratorMessage):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.DroneFlightScenarioGeneratorInfo)
class DroneFlightScenarioGeneratorInfo(pd_spawn_pb2.DroneFlightScenarioGeneratorInfo, NonAtomicGeneratorMessage):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.JaywalkingScenarioGeneratorInfo)
class JaywalkingScenarioGeneratorInfo(pd_spawn_pb2.JaywalkingScenarioGeneratorInfo, NonAtomicGeneratorMessage):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.JunctionScenarioGeneratorInfo)
class JunctionScenarioGeneratorInfo(pd_spawn_pb2.JunctionScenarioGeneratorInfo, NonAtomicGeneratorMessage):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.KittiScenarioGeneratorInfo)
class KittiScenarioGeneratorInfo(pd_spawn_pb2.KittiScenarioGeneratorInfo, NonAtomicGeneratorMessage):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.LaneTypeScenarioGeneratorInfo)
class LaneTypeScenarioGeneratorInfo(pd_spawn_pb2.LaneTypeScenarioGeneratorInfo, NonAtomicGeneratorMessage):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.ParkingScenarioGeneratorInfo)
class ParkingScenarioGeneratorInfo(pd_spawn_pb2.ParkingScenarioGeneratorInfo, NonAtomicGeneratorMessage):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.VehiclePositionScenarioGeneratorInfo)
class VehiclePositionScenarioGeneratorInfo(
    pd_spawn_pb2.VehiclePositionScenarioGeneratorInfo, NonAtomicGeneratorMessage
):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.PropScenarioGeneratorInfo)
class PropScenarioGeneratorInfo(pd_spawn_pb2.PropScenarioGeneratorInfo, NonAtomicGeneratorMessage):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.RandomLaneScenarioGeneratorInfo)
class RandomLaneScenarioGeneratorInfo(pd_spawn_pb2.RandomLaneScenarioGeneratorInfo, NonAtomicGeneratorMessage):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.StaticCamScenarioGeneratorInfo)
class StaticCamScenarioGeneratorInfo(pd_spawn_pb2.StaticCamScenarioGeneratorInfo, NonAtomicGeneratorMessage):
    ...


@register_wrapper(proto_type=pd_spawn_pb2_base.VehicleOfInterestScenarioGeneratorInfo)
class VehicleOfInterestScenarioGeneratorInfo(
    pd_spawn_pb2.VehicleOfInterestScenarioGeneratorInfo, NonAtomicGeneratorMessage
):
    ...
