from pd.internal.proto.keystone.generated.wrapper.pd_distributions_pb2 import CategoricalDistribution, Bucket
from pd.internal.proto.keystone.generated.wrapper.pd_environments_pb2 import EnvironmentPreset


class TestEnvironmentPreset:
    def test_instantiating_environment_preset_with_time_of_day_work(self) -> None:
        # This effectively tests nested proto wrapper access and assignment works
        environment = EnvironmentPreset(
            time_of_day=CategoricalDistribution(
                buckets=[
                    Bucket(int32_value=2),
                    Bucket(int32_value=4),
                ]
            )
        )

        assert len(environment.time_of_day.buckets) == 2
        assert environment.time_of_day.buckets[0].int32_value == 2
        assert environment.time_of_day.buckets[1].int32_value == 4

    def test_reassigning_time_of_day_works(self) -> None:
        # This effectively tests nested proto wrapper access and assignment works
        environment = EnvironmentPreset(
            time_of_day=CategoricalDistribution(
                buckets=[
                    Bucket(int32_value=2),
                    Bucket(int32_value=4),
                ]
            )
        )

        environment.time_of_day = CategoricalDistribution(
            buckets=[
                Bucket(int32_value=1),
                Bucket(int32_value=3),
                Bucket(int32_value=42),
            ]
        )

        assert len(environment.time_of_day.buckets) == 3
        assert environment.time_of_day.buckets[0].int32_value == 1
        assert environment.time_of_day.buckets[1].int32_value == 3
        assert environment.time_of_day.buckets[2].int32_value == 42
        assert environment.proto.time_of_day is environment.time_of_day.proto
        assert environment.proto.time_of_day.buckets[0] is environment.time_of_day.buckets[0].proto

    def test_appending_time_of_day_works(self) -> None:
        environment = EnvironmentPreset(
            time_of_day=CategoricalDistribution(
                buckets=[
                    Bucket(int32_value=2),
                    Bucket(int32_value=4),
                ]
            )
        )

        environment.time_of_day.buckets.append(Bucket(int32_value=42))

        assert len(environment.time_of_day.buckets) == 3
        assert environment.time_of_day.buckets[0].int32_value == 2
        assert environment.time_of_day.buckets[1].int32_value == 4
        assert environment.time_of_day.buckets[2].int32_value == 42
        assert environment.proto.time_of_day is environment.time_of_day.proto
        for i in range(3):
            assert environment.proto.time_of_day.buckets[i] is environment.time_of_day.buckets[i].proto

    def test_it_references_assigned_object_after_setter(self) -> None:
        environment = EnvironmentPreset(
            time_of_day=CategoricalDistribution(
                buckets=[
                    Bucket(int32_value=2),
                    Bucket(int32_value=4),
                ]
            )
        )
        old_time_of_day = environment.time_of_day
        old_buckets = environment.time_of_day.buckets
        old_first_bucket = old_buckets[0]

        new_time_of_day = CategoricalDistribution(
            buckets=[
                Bucket(int32_value=1),
                Bucket(int32_value=3),
                Bucket(int32_value=42),
            ]
        )

        environment.time_of_day = new_time_of_day

        assert environment.time_of_day is not old_time_of_day
        assert environment.time_of_day.buckets is not old_buckets
        assert environment.time_of_day.buckets[0] is not old_first_bucket
        assert environment.time_of_day is new_time_of_day
        assert environment.time_of_day.buckets is new_time_of_day.buckets
        assert environment.time_of_day.proto == new_time_of_day.proto
