# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class SensorExtrinsicConfigFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSensorExtrinsicConfigFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SensorExtrinsicConfigFB()
        x.Init(buf, n + offset)
        return x

    # SensorExtrinsicConfigFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SensorExtrinsicConfigFB
    def SensorToVehicle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from .float4x4_t import float4x4_t
            obj = float4x4_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SensorExtrinsicConfigFB
    def LockToYaw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # SensorExtrinsicConfigFB
    def AttachSocket(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # SensorExtrinsicConfigFB
    def FollowRotation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 1

def SensorExtrinsicConfigFBStart(builder): builder.StartObject(4)
def SensorExtrinsicConfigFBAddSensorToVehicle(builder, sensorToVehicle): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(sensorToVehicle), 0)
def SensorExtrinsicConfigFBAddLockToYaw(builder, lockToYaw): builder.PrependBoolSlot(1, lockToYaw, 0)
def SensorExtrinsicConfigFBAddAttachSocket(builder, attachSocket): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(attachSocket), 0)
def SensorExtrinsicConfigFBAddFollowRotation(builder, followRotation): builder.PrependBoolSlot(3, followRotation, 1)
def SensorExtrinsicConfigFBEnd(builder): return builder.EndObject()