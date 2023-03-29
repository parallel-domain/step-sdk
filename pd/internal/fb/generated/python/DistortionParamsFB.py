# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class DistortionParamsFB(object):
    __slots__ = ['_tab']

    # DistortionParamsFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DistortionParamsFB
    def K1(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # DistortionParamsFB
    def K2(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # DistortionParamsFB
    def K3(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # DistortionParamsFB
    def K4(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(12))
    # DistortionParamsFB
    def K5(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(16))
    # DistortionParamsFB
    def K6(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(20))
    # DistortionParamsFB
    def P1(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(24))
    # DistortionParamsFB
    def P2(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(28))
    # DistortionParamsFB
    def Skew(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(32))
    # DistortionParamsFB
    def IsFisheye(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(36))
    # DistortionParamsFB
    def Fx(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(40))
    # DistortionParamsFB
    def Fy(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(44))
    # DistortionParamsFB
    def Cx(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(48))
    # DistortionParamsFB
    def Cy(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(52))

def CreateDistortionParamsFB(builder, k1, k2, k3, k4, k5, k6, p1, p2, skew, isFisheye, fx, fy, cx, cy):
    builder.Prep(4, 56)
    builder.PrependFloat32(cy)
    builder.PrependFloat32(cx)
    builder.PrependFloat32(fy)
    builder.PrependFloat32(fx)
    builder.Pad(3)
    builder.PrependBool(isFisheye)
    builder.PrependFloat32(skew)
    builder.PrependFloat32(p2)
    builder.PrependFloat32(p1)
    builder.PrependFloat32(k6)
    builder.PrependFloat32(k5)
    builder.PrependFloat32(k4)
    builder.PrependFloat32(k3)
    builder.PrependFloat32(k2)
    builder.PrependFloat32(k1)
    return builder.Offset()
