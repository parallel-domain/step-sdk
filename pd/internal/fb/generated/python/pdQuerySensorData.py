# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdQuerySensorData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspdQuerySensorData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pdQuerySensorData()
        x.Init(buf, n + offset)
        return x

    # pdQuerySensorData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pdQuerySensorData
    def AgentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # pdQuerySensorData
    def SensorName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # pdQuerySensorData
    def BufferType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def pdQuerySensorDataStart(builder): builder.StartObject(3)
def pdQuerySensorDataAddAgentId(builder, agentId): builder.PrependUint64Slot(0, agentId, 0)
def pdQuerySensorDataAddSensorName(builder, sensorName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(sensorName), 0)
def pdQuerySensorDataAddBufferType(builder, bufferType): builder.PrependUint8Slot(2, bufferType, 0)
def pdQuerySensorDataEnd(builder): return builder.EndObject()
