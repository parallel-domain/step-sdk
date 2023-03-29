# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class AgentIntersectionStatusFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAgentIntersectionStatusFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AgentIntersectionStatusFB()
        x.Init(buf, n + offset)
        return x

    # AgentIntersectionStatusFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AgentIntersectionStatusFB
    def AgentId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # AgentIntersectionStatusFB
    def Arrived(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # AgentIntersectionStatusFB
    def ArrivalTimeS(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AgentIntersectionStatusFB
    def HasUpcomingStop(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # AgentIntersectionStatusFB
    def LengthToStopM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AgentIntersectionStatusFB
    def InsideJunctionLaneOccupied(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

def AgentIntersectionStatusFBStart(builder): builder.StartObject(6)
def AgentIntersectionStatusFBAddAgentId(builder, agentId): builder.PrependUint64Slot(0, agentId, 0)
def AgentIntersectionStatusFBAddArrived(builder, arrived): builder.PrependBoolSlot(1, arrived, 0)
def AgentIntersectionStatusFBAddArrivalTimeS(builder, arrivalTimeS): builder.PrependFloat32Slot(2, arrivalTimeS, 0.0)
def AgentIntersectionStatusFBAddHasUpcomingStop(builder, hasUpcomingStop): builder.PrependBoolSlot(3, hasUpcomingStop, 0)
def AgentIntersectionStatusFBAddLengthToStopM(builder, lengthToStopM): builder.PrependFloat32Slot(4, lengthToStopM, 0.0)
def AgentIntersectionStatusFBAddInsideJunctionLaneOccupied(builder, insideJunctionLaneOccupied): builder.PrependBoolSlot(5, insideJunctionLaneOccupied, 0)
def AgentIntersectionStatusFBEnd(builder): return builder.EndObject()
