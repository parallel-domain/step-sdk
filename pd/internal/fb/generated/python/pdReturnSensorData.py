# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdReturnSensorData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspdReturnSensorData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pdReturnSensorData()
        x.Init(buf, n + offset)
        return x

    # pdReturnSensorData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pdReturnSensorData
    def Width(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # pdReturnSensorData
    def Height(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # pdReturnSensorData
    def Channel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # pdReturnSensorData
    def Data(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # pdReturnSensorData
    def DataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # pdReturnSensorData
    def DataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def pdReturnSensorDataStart(builder): builder.StartObject(4)
def pdReturnSensorDataAddWidth(builder, width): builder.PrependUint32Slot(0, width, 0)
def pdReturnSensorDataAddHeight(builder, height): builder.PrependUint32Slot(1, height, 0)
def pdReturnSensorDataAddChannel(builder, channel): builder.PrependUint32Slot(2, channel, 0)
def pdReturnSensorDataAddData(builder, data): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(data), 0)
def pdReturnSensorDataStartDataVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def pdReturnSensorDataEnd(builder): return builder.EndObject()
