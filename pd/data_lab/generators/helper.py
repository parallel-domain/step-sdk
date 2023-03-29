# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

from typing import List, Union

from pd.data_lab.generators.non_atomics import NonAtomicGeneratorMessage
from pd.internal.proto.keystone.generated.python.pd_spawn_pb2 import GeneratorConfigPreset
from pd.internal.proto.keystone.generated.python.pd_unified_generator_pb2 import (
    AtomicGeneratorParameters,
    UnifiedGeneratorParameters,
)
from pd.internal.proto.keystone.generated.wrapper.pd_unified_generator_pb2 import (
    DebrisGeneratorParameters,
    DroneGeneratorParameters,
    EgoAgentGeneratorParameters,
    ParkedVehicleGeneratorParameters,
    PedestrianGeneratorParameters,
    RandomPedestrianGeneratorParameters,
    StaticAgentGeneratorParameters,
    TrafficGeneratorParameters,
    VehicleGeneratorParameters,
)
from pd.internal.proto.keystone.generated.wrapper.utils import AtomicGeneratorMessage, get_wrapper


def decode_generators_message(generators: UnifiedGeneratorParameters) -> List[AtomicGeneratorMessage]:
    decoded_gens = list()
    for gen in generators.atomics:
        field_name = gen.WhichOneof("parameters")
        obj = getattr(gen, field_name)
        wrapped = get_wrapper(obj.__class__)(proto=obj)
        decoded_gens.append(wrapped)
    return decoded_gens


def decode_generator_preset(
    generator_preset: GeneratorConfigPreset,
) -> Union[List[AtomicGeneratorMessage], List[NonAtomicGeneratorMessage]]:
    attr_name = generator_preset.WhichOneof("generator")
    if attr_name == "unified_generator":
        return decode_generators_message(generators=generator_preset.unified_generator)
    else:
        non_atomic_gen = getattr(generator_preset, attr_name)
        wrapped = get_wrapper(non_atomic_gen.__class__)(proto=non_atomic_gen)
        return [wrapped]


def encode_atomic_generator(config: AtomicGeneratorMessage) -> AtomicGeneratorParameters:
    if isinstance(config, StaticAgentGeneratorParameters):
        return AtomicGeneratorParameters(static_agent=config.proto)
    elif isinstance(config, VehicleGeneratorParameters):
        return AtomicGeneratorParameters(vehicle=config.proto)
    elif isinstance(config, EgoAgentGeneratorParameters):
        return AtomicGeneratorParameters(ego_agent=config.proto)
    elif isinstance(config, TrafficGeneratorParameters):
        return AtomicGeneratorParameters(traffic=config.proto)
    elif isinstance(config, DebrisGeneratorParameters):
        return AtomicGeneratorParameters(debris=config.proto)
    elif isinstance(config, PedestrianGeneratorParameters):
        return AtomicGeneratorParameters(pedestrian=config.proto)
    elif isinstance(config, ParkedVehicleGeneratorParameters):
        return AtomicGeneratorParameters(parked_vehicles=config.proto)
    elif isinstance(config, DroneGeneratorParameters):
        return AtomicGeneratorParameters(drone=config.proto)
    elif isinstance(config, RandomPedestrianGeneratorParameters):
        return AtomicGeneratorParameters(random_pedestrian=config.proto)
    else:
        raise NotImplementedError(f"Atomic generator of type {type(config)} is not supported")
