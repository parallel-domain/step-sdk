# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdQueryStateData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspdQueryStateData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pdQueryStateData()
        x.Init(buf, n + offset)
        return x

    # pdQueryStateData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def pdQueryStateDataStart(builder): builder.StartObject(0)
def pdQueryStateDataEnd(builder): return builder.EndObject()