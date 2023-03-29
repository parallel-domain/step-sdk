# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class SimpleVehicleStateFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSimpleVehicleStateFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SimpleVehicleStateFB()
        x.Init(buf, n + offset)
        return x

    # SimpleVehicleStateFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SimpleVehicleStateFB
    def WheelToWorld(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 64
            from .float4x4_t import float4x4_t
            obj = float4x4_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SimpleVehicleStateFB
    def WheelToWorldLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SimpleVehicleStateFB
    def Acceleration(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # SimpleVehicleStateFB
    def EngineRotationSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # SimpleVehicleStateFB
    def HandbrakeOn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # SimpleVehicleStateFB
    def EmergencyLightsOn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # SimpleVehicleStateFB
    def AccelerationValid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # SimpleVehicleStateFB
    def AccelerationVector(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            x = o + self._tab.Pos
            from .float3_t import float3_t
            obj = float3_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SimpleVehicleStateFB
    def RoadWheelAngleRad(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # SimpleVehicleStateFB
    def RoadWheelAngleRateRadps(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # SimpleVehicleStateFB
    def WheelStates(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .WheelStateFB import WheelStateFB
            obj = WheelStateFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SimpleVehicleStateFB
    def WheelStatesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SimpleVehicleStateFB
    def HasBrakeLightOn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # SimpleVehicleStateFB
    def BrakeLightOn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # SimpleVehicleStateFB
    def WorldState(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .WorldStateFB import WorldStateFB
            obj = WorldStateFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SimpleVehicleStateFB
    def Vehicle2dMotion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Vehicle2DMotionFB import Vehicle2DMotionFB
            obj = Vehicle2DMotionFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SimpleVehicleStateFB
    def Gear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def SimpleVehicleStateFBStart(builder): builder.StartObject(21)
def SimpleVehicleStateFBAddWheelToWorld(builder, wheelToWorld): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(wheelToWorld), 0)
def SimpleVehicleStateFBStartWheelToWorldVector(builder, numElems): return builder.StartVector(64, numElems, 4)
def SimpleVehicleStateFBAddAcceleration(builder, acceleration): builder.PrependFloat32Slot(1, acceleration, 0.0)
def SimpleVehicleStateFBAddEngineRotationSpeed(builder, engineRotationSpeed): builder.PrependFloat32Slot(6, engineRotationSpeed, 0.0)
def SimpleVehicleStateFBAddHandbrakeOn(builder, handbrakeOn): builder.PrependBoolSlot(7, handbrakeOn, 0)
def SimpleVehicleStateFBAddEmergencyLightsOn(builder, emergencyLightsOn): builder.PrependBoolSlot(8, emergencyLightsOn, 0)
def SimpleVehicleStateFBAddAccelerationValid(builder, accelerationValid): builder.PrependBoolSlot(9, accelerationValid, 0)
def SimpleVehicleStateFBAddAccelerationVector(builder, accelerationVector): builder.PrependStructSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(accelerationVector), 0)
def SimpleVehicleStateFBAddRoadWheelAngleRad(builder, roadWheelAngleRad): builder.PrependFloat32Slot(13, roadWheelAngleRad, 0.0)
def SimpleVehicleStateFBAddRoadWheelAngleRateRadps(builder, roadWheelAngleRateRadps): builder.PrependFloat32Slot(14, roadWheelAngleRateRadps, 0.0)
def SimpleVehicleStateFBAddWheelStates(builder, wheelStates): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(wheelStates), 0)
def SimpleVehicleStateFBStartWheelStatesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def SimpleVehicleStateFBAddHasBrakeLightOn(builder, hasBrakeLightOn): builder.PrependBoolSlot(16, hasBrakeLightOn, 0)
def SimpleVehicleStateFBAddBrakeLightOn(builder, brakeLightOn): builder.PrependBoolSlot(17, brakeLightOn, 0)
def SimpleVehicleStateFBAddWorldState(builder, worldState): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(worldState), 0)
def SimpleVehicleStateFBAddVehicle2dMotion(builder, vehicle2dMotion): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(vehicle2dMotion), 0)
def SimpleVehicleStateFBAddGear(builder, gear): builder.PrependInt8Slot(20, gear, 0)
def SimpleVehicleStateFBEnd(builder): return builder.EndObject()