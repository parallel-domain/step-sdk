# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdReturnAnnotation2DData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspdReturnAnnotation2DData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pdReturnAnnotation2DData()
        x.Init(buf, n + offset)
        return x

    # pdReturnAnnotation2DData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pdReturnAnnotation2DData
    def Num(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # pdReturnAnnotation2DData
    def Annotation2d(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .pdAnnotation2DData import pdAnnotation2DData
            obj = pdAnnotation2DData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # pdReturnAnnotation2DData
    def Annotation2dLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def pdReturnAnnotation2DDataStart(builder): builder.StartObject(2)
def pdReturnAnnotation2DDataAddNum(builder, num): builder.PrependUint32Slot(0, num, 0)
def pdReturnAnnotation2DDataAddAnnotation2d(builder, annotation2d): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(annotation2d), 0)
def pdReturnAnnotation2DDataStartAnnotation2dVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def pdReturnAnnotation2DDataEnd(builder): return builder.EndObject()
