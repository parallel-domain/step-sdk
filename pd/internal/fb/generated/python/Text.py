# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class Text(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsText(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Text()
        x.Init(buf, n + offset)
        return x

    # Text
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Text
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

def TextStart(builder): builder.StartObject(1)
def TextAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def TextEnd(builder): return builder.EndObject()
