# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class SimpleControlStateFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSimpleControlStateFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SimpleControlStateFB()
        x.Init(buf, n + offset)
        return x

    # SimpleControlStateFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SimpleControlStateFB
    def Steering(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # SimpleControlStateFB
    def Accelerate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # SimpleControlStateFB
    def Brake(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # SimpleControlStateFB
    def Clutch(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # SimpleControlStateFB
    def Handbrake(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # SimpleControlStateFB
    def Gear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

def SimpleControlStateFBStart(builder): builder.StartObject(6)
def SimpleControlStateFBAddSteering(builder, steering): builder.PrependFloat32Slot(0, steering, 0.0)
def SimpleControlStateFBAddAccelerate(builder, accelerate): builder.PrependFloat32Slot(1, accelerate, 0.0)
def SimpleControlStateFBAddBrake(builder, brake): builder.PrependFloat32Slot(2, brake, 0.0)
def SimpleControlStateFBAddClutch(builder, clutch): builder.PrependFloat32Slot(3, clutch, 0.0)
def SimpleControlStateFBAddHandbrake(builder, handbrake): builder.PrependFloat32Slot(4, handbrake, 0.0)
def SimpleControlStateFBAddGear(builder, gear): builder.PrependInt16Slot(5, gear, 0)
def SimpleControlStateFBEnd(builder): return builder.EndObject()
