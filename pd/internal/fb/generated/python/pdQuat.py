# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdQuat(object):
    __slots__ = ['_tab']

    # pdQuat
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pdQuat
    def W(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # pdQuat
    def X(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # pdQuat
    def Y(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # pdQuat
    def Z(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(12))

def CreatepdQuat(builder, w, x, y, z):
    builder.Prep(4, 16)
    builder.PrependFloat32(z)
    builder.PrependFloat32(y)
    builder.PrependFloat32(x)
    builder.PrependFloat32(w)
    return builder.Offset()