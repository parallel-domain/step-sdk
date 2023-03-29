# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class PIDConfigFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPIDConfigFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PIDConfigFB()
        x.Init(buf, n + offset)
        return x

    # PIDConfigFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PIDConfigFB
    def P(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # PIDConfigFB
    def I(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # PIDConfigFB
    def D(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # PIDConfigFB
    def S(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # PIDConfigFB
    def IntegralBlend(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # PIDConfigFB
    def OutputMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # PIDConfigFB
    def OutputMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # PIDConfigFB
    def ClampI(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # PIDConfigFB
    def IMin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # PIDConfigFB
    def IMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def PIDConfigFBStart(builder): builder.StartObject(10)
def PIDConfigFBAddP(builder, p): builder.PrependFloat32Slot(0, p, 0.0)
def PIDConfigFBAddI(builder, i): builder.PrependFloat32Slot(1, i, 0.0)
def PIDConfigFBAddD(builder, d): builder.PrependFloat32Slot(2, d, 0.0)
def PIDConfigFBAddS(builder, s): builder.PrependFloat32Slot(3, s, 0.0)
def PIDConfigFBAddIntegralBlend(builder, integralBlend): builder.PrependFloat32Slot(4, integralBlend, 0.0)
def PIDConfigFBAddOutputMin(builder, outputMin): builder.PrependFloat32Slot(5, outputMin, 0.0)
def PIDConfigFBAddOutputMax(builder, outputMax): builder.PrependFloat32Slot(6, outputMax, 0.0)
def PIDConfigFBAddClampI(builder, clampI): builder.PrependBoolSlot(7, clampI, 0)
def PIDConfigFBAddIMin(builder, iMin): builder.PrependFloat32Slot(8, iMin, 0.0)
def PIDConfigFBAddIMax(builder, iMax): builder.PrependFloat32Slot(9, iMax, 0.0)
def PIDConfigFBEnd(builder): return builder.EndObject()