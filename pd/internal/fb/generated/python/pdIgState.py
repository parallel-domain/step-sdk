# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdIgState(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspdIgState(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pdIgState()
        x.Init(buf, n + offset)
        return x

    # pdIgState
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pdIgState
    def IgState(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def pdIgStateStart(builder): builder.StartObject(1)
def pdIgStateAddIgState(builder, igState): builder.PrependUint8Slot(0, igState, 0)
def pdIgStateEnd(builder): return builder.EndObject()
