# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class VehiclePlannerOutputFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsVehiclePlannerOutputFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = VehiclePlannerOutputFB()
        x.Init(buf, n + offset)
        return x

    # VehiclePlannerOutputFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # VehiclePlannerOutputFB
    def Points(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .PlanPointFB import PlanPointFB
            obj = PlanPointFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # VehiclePlannerOutputFB
    def PointsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def VehiclePlannerOutputFBStart(builder): builder.StartObject(1)
def VehiclePlannerOutputFBAddPoints(builder, points): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(points), 0)
def VehiclePlannerOutputFBStartPointsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def VehiclePlannerOutputFBEnd(builder): return builder.EndObject()