# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class SensorConfigFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSensorConfigFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SensorConfigFB()
        x.Init(buf, n + offset)
        return x

    # SensorConfigFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SensorConfigFB
    def DisplayName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # SensorConfigFB
    def SensorIntrinsicType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # SensorConfigFB
    def SensorIntrinsic(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # SensorConfigFB
    def SensorExtrinsic(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .SensorExtrinsicConfigFB import SensorExtrinsicConfigFB
            obj = SensorExtrinsicConfigFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SensorConfigFB
    def RenderEgo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

def SensorConfigFBStart(builder): builder.StartObject(5)
def SensorConfigFBAddDisplayName(builder, displayName): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(displayName), 0)
def SensorConfigFBAddSensorIntrinsicType(builder, sensorIntrinsicType): builder.PrependUint8Slot(1, sensorIntrinsicType, 0)
def SensorConfigFBAddSensorIntrinsic(builder, sensorIntrinsic): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(sensorIntrinsic), 0)
def SensorConfigFBAddSensorExtrinsic(builder, sensorExtrinsic): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(sensorExtrinsic), 0)
def SensorConfigFBAddRenderEgo(builder, renderEgo): builder.PrependBoolSlot(4, renderEgo, 0)
def SensorConfigFBEnd(builder): return builder.EndObject()
