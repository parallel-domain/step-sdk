def test_internal_imports_keystone():
    """Internal keystone interfaces can be imported successfully"""
    from pd.internal.proto.keystone.generated.python.pd_render_pb2 import RenderInfo
    assert(RenderInfo)
    from pd.internal.proto.keystone.generated.python.pd_scenario_pb2 import ScenarioGenConfig
    assert(ScenarioGenConfig)


def test_internal_imports_label_engine():
    """Internal label-engine interfaces can be imported successfully"""
    from pd.internal.proto.label_engine.generated.python.mesh_map_pb2 import Mesh
    assert(Mesh)
    from pd.internal.proto.label_engine.generated.python.dgpv1.dataset_pb2 import Ontology
    assert(Ontology)
    from pd.internal.proto.label_engine.generated.python.dgpv1.contribs.pd.metadata_pb2 import SceneType
    assert(SceneType)
