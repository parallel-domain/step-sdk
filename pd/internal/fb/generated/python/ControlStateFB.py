# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class ControlStateFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsControlStateFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ControlStateFB()
        x.Init(buf, n + offset)
        return x

    # ControlStateFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ControlStateFB
    def VehicleVector(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from .float3_t import float3_t
            obj = float3_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ControlStateFB
    def TargetVector(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from .float3_t import float3_t
            obj = float3_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ControlStateFB
    def Velocity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .float3_t import float3_t
            obj = float3_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ControlStateFB
    def DotProd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlStateFB
    def PerpDot(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlStateFB
    def Error(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlStateFB
    def Steering(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlStateFB
    def Accelerate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlStateFB
    def Brake(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlStateFB
    def SteeringController(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .PIDControllerFB import PIDControllerFB
            obj = PIDControllerFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ControlStateFB
    def AccelerateController(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .PIDControllerFB import PIDControllerFB
            obj = PIDControllerFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ControlStateFB
    def StopController(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .PIDControllerFB import PIDControllerFB
            obj = PIDControllerFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ControlStateFB
    def ObstacleDistance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlStateFB
    def IndicatorState(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ControlStateFB
    def Gear(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 1

    # ControlStateFB
    def TargetSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlStateFB
    def TargetAccelValid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # ControlStateFB
    def TargetAccelMps2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlStateFB
    def FilteredAccelValid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # ControlStateFB
    def FilteredAccelMps2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlStateFB
    def AccelLimitsMps2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .KinematicLimits import KinematicLimits
            obj = KinematicLimits()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ControlStateFB
    def JerkLimitsMps3(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .KinematicLimits import KinematicLimits
            obj = KinematicLimits()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ControlStateFB
    def BrakeUntilEgoTimeToAgentMet(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

def ControlStateFBStart(builder): builder.StartObject(23)
def ControlStateFBAddVehicleVector(builder, vehicleVector): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(vehicleVector), 0)
def ControlStateFBAddTargetVector(builder, targetVector): builder.PrependStructSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(targetVector), 0)
def ControlStateFBAddVelocity(builder, velocity): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(velocity), 0)
def ControlStateFBAddDotProd(builder, dotProd): builder.PrependFloat32Slot(3, dotProd, 0.0)
def ControlStateFBAddPerpDot(builder, perpDot): builder.PrependFloat32Slot(4, perpDot, 0.0)
def ControlStateFBAddError(builder, error): builder.PrependFloat32Slot(5, error, 0.0)
def ControlStateFBAddSteering(builder, steering): builder.PrependFloat32Slot(6, steering, 0.0)
def ControlStateFBAddAccelerate(builder, accelerate): builder.PrependFloat32Slot(7, accelerate, 0.0)
def ControlStateFBAddBrake(builder, brake): builder.PrependFloat32Slot(8, brake, 0.0)
def ControlStateFBAddSteeringController(builder, steeringController): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(steeringController), 0)
def ControlStateFBAddAccelerateController(builder, accelerateController): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(accelerateController), 0)
def ControlStateFBAddStopController(builder, stopController): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(stopController), 0)
def ControlStateFBAddObstacleDistance(builder, obstacleDistance): builder.PrependFloat32Slot(12, obstacleDistance, 0.0)
def ControlStateFBAddIndicatorState(builder, indicatorState): builder.PrependInt32Slot(13, indicatorState, 0)
def ControlStateFBAddGear(builder, gear): builder.PrependInt8Slot(14, gear, 1)
def ControlStateFBAddTargetSpeed(builder, targetSpeed): builder.PrependFloat32Slot(15, targetSpeed, 0.0)
def ControlStateFBAddTargetAccelValid(builder, targetAccelValid): builder.PrependBoolSlot(16, targetAccelValid, 0)
def ControlStateFBAddTargetAccelMps2(builder, targetAccelMps2): builder.PrependFloat32Slot(17, targetAccelMps2, 0.0)
def ControlStateFBAddFilteredAccelValid(builder, filteredAccelValid): builder.PrependBoolSlot(18, filteredAccelValid, 0)
def ControlStateFBAddFilteredAccelMps2(builder, filteredAccelMps2): builder.PrependFloat32Slot(19, filteredAccelMps2, 0.0)
def ControlStateFBAddAccelLimitsMps2(builder, accelLimitsMps2): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(accelLimitsMps2), 0)
def ControlStateFBAddJerkLimitsMps3(builder, jerkLimitsMps3): builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(jerkLimitsMps3), 0)
def ControlStateFBAddBrakeUntilEgoTimeToAgentMet(builder, brakeUntilEgoTimeToAgentMet): builder.PrependBoolSlot(22, brakeUntilEgoTimeToAgentMet, 0)
def ControlStateFBEnd(builder): return builder.EndObject()
