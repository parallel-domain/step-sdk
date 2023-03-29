# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class VehicleTrafficControlOutputFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsVehicleTrafficControlOutputFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = VehicleTrafficControlOutputFB()
        x.Init(buf, n + offset)
        return x

    # VehicleTrafficControlOutputFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # VehicleTrafficControlOutputFB
    def TrafficControls(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .VehicleTrafficControlFB import VehicleTrafficControlFB
            obj = VehicleTrafficControlFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # VehicleTrafficControlOutputFB
    def TrafficControlsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def VehicleTrafficControlOutputFBStart(builder): builder.StartObject(1)
def VehicleTrafficControlOutputFBAddTrafficControls(builder, trafficControls): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(trafficControls), 0)
def VehicleTrafficControlOutputFBStartTrafficControlsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def VehicleTrafficControlOutputFBEnd(builder): return builder.EndObject()
