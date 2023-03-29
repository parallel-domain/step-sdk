# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class TrafficLightObjectFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTrafficLightObjectFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TrafficLightObjectFB()
        x.Init(buf, n + offset)
        return x

    # TrafficLightObjectFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TrafficLightObjectFB
    def SignaledIntersectionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # TrafficLightObjectFB
    def PhaseId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # TrafficLightObjectFB
    def Position(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .float3_t import float3_t
            obj = float3_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def TrafficLightObjectFBStart(builder): builder.StartObject(3)
def TrafficLightObjectFBAddSignaledIntersectionId(builder, signaledIntersectionId): builder.PrependUint64Slot(0, signaledIntersectionId, 0)
def TrafficLightObjectFBAddPhaseId(builder, phaseId): builder.PrependUint64Slot(1, phaseId, 0)
def TrafficLightObjectFBAddPosition(builder, position): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(position), 0)
def TrafficLightObjectFBEnd(builder): return builder.EndObject()