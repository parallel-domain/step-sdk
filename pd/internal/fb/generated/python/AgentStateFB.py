# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class AgentStateFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAgentStateFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AgentStateFB()
        x.Init(buf, n + offset)
        return x

    # AgentStateFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AgentStateFB
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # AgentStateFB
    def State(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .StateObjectFB import StateObjectFB
            obj = StateObjectFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # AgentStateFB
    def StateLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # AgentStateFB
    def Modules(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # AgentStateFB
    def ModulesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # AgentStateFB
    def ModulesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def AgentStateFBStart(builder): builder.StartObject(3)
def AgentStateFBAddId(builder, id): builder.PrependUint64Slot(0, id, 0)
def AgentStateFBAddState(builder, state): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(state), 0)
def AgentStateFBStartStateVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def AgentStateFBAddModules(builder, modules): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(modules), 0)
def AgentStateFBStartModulesVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def AgentStateFBEnd(builder): return builder.EndObject()
