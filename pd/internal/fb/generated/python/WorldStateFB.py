# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class WorldStateFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsWorldStateFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WorldStateFB()
        x.Init(buf, n + offset)
        return x

    # WorldStateFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # WorldStateFB
    def Pose(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from .float4x4_t import float4x4_t
            obj = float4x4_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WorldStateFB
    def VelocityMps(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from .float3_t import float3_t
            obj = float3_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WorldStateFB
    def AccelerationMps2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .float3_t import float3_t
            obj = float3_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WorldStateFB
    def JerkMps3(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = o + self._tab.Pos
            from .float3_t import float3_t
            obj = float3_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def WorldStateFBStart(builder): builder.StartObject(4)
def WorldStateFBAddPose(builder, pose): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(pose), 0)
def WorldStateFBAddVelocityMps(builder, velocityMps): builder.PrependStructSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(velocityMps), 0)
def WorldStateFBAddAccelerationMps2(builder, accelerationMps2): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(accelerationMps2), 0)
def WorldStateFBAddJerkMps3(builder, jerkMps3): builder.PrependStructSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(jerkMps3), 0)
def WorldStateFBEnd(builder): return builder.EndObject()
