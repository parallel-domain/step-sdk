# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdQueryAnnotationData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspdQueryAnnotationData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pdQueryAnnotationData()
        x.Init(buf, n + offset)
        return x

    # pdQueryAnnotationData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pdQueryAnnotationData
    def AgentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # pdQueryAnnotationData
    def SensorName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # pdQueryAnnotationData
    def AnnotationType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def pdQueryAnnotationDataStart(builder): builder.StartObject(3)
def pdQueryAnnotationDataAddAgentId(builder, agentId): builder.PrependUint64Slot(0, agentId, 0)
def pdQueryAnnotationDataAddSensorName(builder, sensorName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(sensorName), 0)
def pdQueryAnnotationDataAddAnnotationType(builder, annotationType): builder.PrependUint8Slot(2, annotationType, 0)
def pdQueryAnnotationDataEnd(builder): return builder.EndObject()
