# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdReturnAnnotation3DData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspdReturnAnnotation3DData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pdReturnAnnotation3DData()
        x.Init(buf, n + offset)
        return x

    # pdReturnAnnotation3DData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pdReturnAnnotation3DData
    def Num(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # pdReturnAnnotation3DData
    def Annotation3d(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .pdAnnotation3DData import pdAnnotation3DData
            obj = pdAnnotation3DData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # pdReturnAnnotation3DData
    def Annotation3dLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def pdReturnAnnotation3DDataStart(builder): builder.StartObject(2)
def pdReturnAnnotation3DDataAddNum(builder, num): builder.PrependUint32Slot(0, num, 0)
def pdReturnAnnotation3DDataAddAnnotation3d(builder, annotation3d): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(annotation3d), 0)
def pdReturnAnnotation3DDataStartAnnotation3dVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def pdReturnAnnotation3DDataEnd(builder): return builder.EndObject()
