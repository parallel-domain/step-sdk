# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class float3_t(object):
    __slots__ = ['_tab']

    # float3_t
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # float3_t
    def X(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # float3_t
    def Y(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # float3_t
    def Z(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))

def Createfloat3_t(builder, x, y, z):
    builder.Prep(4, 12)
    builder.PrependFloat32(z)
    builder.PrependFloat32(y)
    builder.PrependFloat32(x)
    return builder.Offset()
