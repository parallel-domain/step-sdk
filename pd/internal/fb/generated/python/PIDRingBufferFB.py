# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class PIDRingBufferFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPIDRingBufferFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PIDRingBufferFB()
        x.Init(buf, n + offset)
        return x

    # PIDRingBufferFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PIDRingBufferFB
    def BufferSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # PIDRingBufferFB
    def Values(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # PIDRingBufferFB
    def ValuesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # PIDRingBufferFB
    def ValuesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def PIDRingBufferFBStart(builder): builder.StartObject(2)
def PIDRingBufferFBAddBufferSize(builder, bufferSize): builder.PrependUint32Slot(0, bufferSize, 0)
def PIDRingBufferFBAddValues(builder, values): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(values), 0)
def PIDRingBufferFBStartValuesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def PIDRingBufferFBEnd(builder): return builder.EndObject()
