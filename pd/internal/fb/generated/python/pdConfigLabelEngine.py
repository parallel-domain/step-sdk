# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdConfigLabelEngine(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspdConfigLabelEngine(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pdConfigLabelEngine()
        x.Init(buf, n + offset)
        return x

    # pdConfigLabelEngine
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pdConfigLabelEngine
    def Config(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # pdConfigLabelEngine
    def SceneName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

def pdConfigLabelEngineStart(builder): builder.StartObject(2)
def pdConfigLabelEngineAddConfig(builder, config): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(config), 0)
def pdConfigLabelEngineAddSceneName(builder, sceneName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(sceneName), 0)
def pdConfigLabelEngineEnd(builder): return builder.EndObject()
