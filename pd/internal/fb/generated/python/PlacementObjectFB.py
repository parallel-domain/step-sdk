# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class PlacementObjectFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPlacementObjectFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PlacementObjectFB()
        x.Init(buf, n + offset)
        return x

    # PlacementObjectFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PlacementObjectFB
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # PlacementObjectFB
    def PlacementType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # PlacementObjectFB
    def Placement(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def PlacementObjectFBStart(builder): builder.StartObject(3)
def PlacementObjectFBAddId(builder, id): builder.PrependUint64Slot(0, id, 0)
def PlacementObjectFBAddPlacementType(builder, placementType): builder.PrependUint8Slot(1, placementType, 0)
def PlacementObjectFBAddPlacement(builder, placement): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(placement), 0)
def PlacementObjectFBEnd(builder): return builder.EndObject()
