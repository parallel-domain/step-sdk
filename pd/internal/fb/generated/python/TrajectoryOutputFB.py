# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class TrajectoryOutputFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTrajectoryOutputFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TrajectoryOutputFB()
        x.Init(buf, n + offset)
        return x

    # TrajectoryOutputFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TrajectoryOutputFB
    def Points(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .TrajectoryPointFB import TrajectoryPointFB
            obj = TrajectoryPointFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TrajectoryOutputFB
    def PointsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def TrajectoryOutputFBStart(builder): builder.StartObject(1)
def TrajectoryOutputFBAddPoints(builder, points): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(points), 0)
def TrajectoryOutputFBStartPointsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def TrajectoryOutputFBEnd(builder): return builder.EndObject()
