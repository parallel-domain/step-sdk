# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class LateralOffsetRequestFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLateralOffsetRequestFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LateralOffsetRequestFB()
        x.Init(buf, n + offset)
        return x

    # LateralOffsetRequestFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # LateralOffsetRequestFB
    def Tmp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

def LateralOffsetRequestFBStart(builder): builder.StartObject(1)
def LateralOffsetRequestFBAddTmp(builder, tmp): builder.PrependUint64Slot(0, tmp, 0)
def LateralOffsetRequestFBEnd(builder): return builder.EndObject()