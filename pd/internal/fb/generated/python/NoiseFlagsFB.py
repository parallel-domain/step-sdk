# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class NoiseFlagsFB(object):
    __slots__ = ['_tab']

    # NoiseFlagsFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NoiseFlagsFB
    def Deprecated(self): return self._tab.Get(flatbuffers.number_types.BoolFlags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))

def CreateNoiseFlagsFB(builder, deprecated):
    builder.Prep(1, 1)
    builder.PrependBool(deprecated)
    return builder.Offset()
