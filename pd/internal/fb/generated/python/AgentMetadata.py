# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class AgentMetadata(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAgentMetadata(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AgentMetadata()
        x.Init(buf, n + offset)
        return x

    # AgentMetadata
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AgentMetadata
    def AgentTags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .AgentTags import AgentTags
            obj = AgentTags()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # AgentMetadata
    def AgentTagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def AgentMetadataStart(builder): builder.StartObject(1)
def AgentMetadataAddAgentTags(builder, agentTags): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(agentTags), 0)
def AgentMetadataStartAgentTagsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def AgentMetadataEnd(builder): return builder.EndObject()
