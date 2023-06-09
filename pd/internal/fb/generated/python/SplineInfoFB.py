# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class SplineInfoFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSplineInfoFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SplineInfoFB()
        x.Init(buf, n + offset)
        return x

    # SplineInfoFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SplineInfoFB
    def Splines(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .SplineFB import SplineFB
            obj = SplineFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SplineInfoFB
    def SplinesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def SplineInfoFBStart(builder): builder.StartObject(1)
def SplineInfoFBAddSplines(builder, splines): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(splines), 0)
def SplineInfoFBStartSplinesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def SplineInfoFBEnd(builder): return builder.EndObject()
