# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class Decal(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsDecal(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Decal()
        x.Init(buf, n + offset)
        return x

    # Decal
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Decal
    def AssetName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

def DecalStart(builder): builder.StartObject(1)
def DecalAddAssetName(builder, assetName): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(assetName), 0)
def DecalEnd(builder): return builder.EndObject()