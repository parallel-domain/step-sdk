# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdReturnLidarSensorData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspdReturnLidarSensorData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pdReturnLidarSensorData()
        x.Init(buf, n + offset)
        return x

    # pdReturnLidarSensorData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pdReturnLidarSensorData
    def NumPoints(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # pdReturnLidarSensorData
    def PointSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # pdReturnLidarSensorData
    def Data(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # pdReturnLidarSensorData
    def DataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # pdReturnLidarSensorData
    def DataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def pdReturnLidarSensorDataStart(builder): builder.StartObject(3)
def pdReturnLidarSensorDataAddNumPoints(builder, numPoints): builder.PrependUint32Slot(0, numPoints, 0)
def pdReturnLidarSensorDataAddPointSize(builder, pointSize): builder.PrependUint32Slot(1, pointSize, 0)
def pdReturnLidarSensorDataAddData(builder, data): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(data), 0)
def pdReturnLidarSensorDataStartDataVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def pdReturnLidarSensorDataEnd(builder): return builder.EndObject()
