from pd.internal.proto.keystone.generated.wrapper.pd_distributions_pb2 import VehicleCategoryWeight
from pd.internal.proto.keystone.generated.wrapper.pd_spawn_pb2 import SpawnConfigPreset, SpawnConfig


class TestSpawnConfig:
    def test_instantiating_intrinsics_with_distortion_parameters_work(self) -> None:
        # This effectively tests nested proto wrapper access and assignment works
        spawn_config = SpawnConfig(
            presets=[
                SpawnConfigPreset(
                    vehicleDistribution={
                        "car": VehicleCategoryWeight(weight=1),
                        "truck": VehicleCategoryWeight(weight=5),
                    }
                )
            ]
        )

        assert set(spawn_config.presets[0].vehicleDistribution.keys()) == {"car", "truck"}
        assert spawn_config.presets[0].vehicleDistribution["car"].weight == 1
        assert spawn_config.presets[0].vehicleDistribution["truck"].weight == 5

    def test_reassigning_presets_works(self) -> None:
        spawn_config = SpawnConfig(
            presets=[
                SpawnConfigPreset(
                    vehicleDistribution={
                        "car": VehicleCategoryWeight(weight=1),
                        "truck": VehicleCategoryWeight(weight=5),
                    }
                )
            ]
        )
        spawn_config.presets = [
            SpawnConfigPreset(
                vehicleDistribution={
                    "pedestrian": VehicleCategoryWeight(weight=2),
                    "truck": VehicleCategoryWeight(weight=10),
                }
            )
        ]

        assert set(spawn_config.presets[0].vehicleDistribution.keys()) == {"pedestrian", "truck"}
        assert spawn_config.presets[0].vehicleDistribution["pedestrian"].weight == 2
        assert spawn_config.presets[0].vehicleDistribution["truck"].weight == 10
        assert spawn_config.proto.presets[0] is spawn_config.presets[0].proto
        for key in ["pedestrian", "truck"]:
            assert (
                spawn_config.proto.presets[0].vehicleDistribution[key]
                is spawn_config.presets[0].vehicleDistribution[key].proto
            )

    def test_reassigning_vehicle_distribution_works(self) -> None:
        spawn_config = SpawnConfig(
            presets=[
                SpawnConfigPreset(
                    vehicleDistribution={
                        "car": VehicleCategoryWeight(weight=1),
                        "truck": VehicleCategoryWeight(weight=5),
                    }
                )
            ]
        )
        spawn_config.presets[0].vehicleDistribution = {
            "pedestrian": VehicleCategoryWeight(weight=2),
            "truck": VehicleCategoryWeight(weight=10),
        }

        assert set(spawn_config.presets[0].vehicleDistribution.keys()) == {"pedestrian", "truck"}
        assert spawn_config.presets[0].vehicleDistribution["pedestrian"].weight == 2
        assert spawn_config.presets[0].vehicleDistribution["truck"].weight == 10
        for key in ["pedestrian", "truck"]:
            assert (
                spawn_config.proto.presets[0].vehicleDistribution[key]
                is spawn_config.presets[0].vehicleDistribution[key].proto
            )

    def test_it_references_assigned_object_after_setter(self) -> None:
        old_car_weight = VehicleCategoryWeight(weight=1)
        old_preset = SpawnConfigPreset(
            vehicleDistribution={
                "car": old_car_weight,
                "truck": VehicleCategoryWeight(weight=5),
            }
        )
        spawn_config = SpawnConfig(presets=[old_preset])

        new_car_weight = VehicleCategoryWeight(weight=2)
        new_preset = SpawnConfigPreset(
            vehicleDistribution={
                "car": new_car_weight,
                "truck": VehicleCategoryWeight(weight=10),
            }
        )
        spawn_config.presets = [new_preset]

        assert spawn_config.presets[0] is not old_preset
        assert spawn_config.presets[0] is new_preset
        assert spawn_config.presets[0].vehicleDistribution["car"] is not old_car_weight
        assert spawn_config.presets[0].vehicleDistribution["car"] is new_car_weight
