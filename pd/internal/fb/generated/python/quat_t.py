# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class quat_t(object):
    __slots__ = ['_tab']

    # quat_t
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # quat_t
    def W(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # quat_t
    def X(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # quat_t
    def Y(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # quat_t
    def Z(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(12))

def Createquat_t(builder, w, x, y, z):
    builder.Prep(4, 16)
    builder.PrependFloat32(z)
    builder.PrependFloat32(y)
    builder.PrependFloat32(x)
    builder.PrependFloat32(w)
    return builder.Offset()
