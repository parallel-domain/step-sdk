# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class ControlConfigFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsControlConfigFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ControlConfigFB()
        x.Init(buf, n + offset)
        return x

    # ControlConfigFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ControlConfigFB
    def Steering(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .PIDConfigFB import PIDConfigFB
            obj = PIDConfigFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ControlConfigFB
    def Accelerate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .PIDConfigFB import PIDConfigFB
            obj = PIDConfigFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ControlConfigFB
    def Stop(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .PIDConfigFB import PIDConfigFB
            obj = PIDConfigFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ControlConfigFB
    def SteeringLookAhead(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlConfigFB
    def AccelerateLookAhead(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlConfigFB
    def TargetSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlConfigFB
    def MaxSinuosity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlConfigFB
    def SinuosityScale(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlConfigFB
    def SteeringMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlConfigFB
    def TargetSeparation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlConfigFB
    def Aggression(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlConfigFB
    def BrakeUntilTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlConfigFB
    def ConstantAccelerate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlConfigFB
    def SignedIntersectionConfigs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .AgentIntersectionConfigFB import AgentIntersectionConfigFB
            obj = AgentIntersectionConfigFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ControlConfigFB
    def SignedIntersectionConfigsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ControlConfigFB
    def BrakeUntilEgoTimeToAgentS(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ControlConfigFB
    def InitialSteeringAngleRad(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def ControlConfigFBStart(builder): builder.StartObject(30)
def ControlConfigFBAddSteering(builder, steering): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(steering), 0)
def ControlConfigFBAddAccelerate(builder, accelerate): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(accelerate), 0)
def ControlConfigFBAddStop(builder, stop): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(stop), 0)
def ControlConfigFBAddSteeringLookAhead(builder, steeringLookAhead): builder.PrependFloat32Slot(3, steeringLookAhead, 0.0)
def ControlConfigFBAddAccelerateLookAhead(builder, accelerateLookAhead): builder.PrependFloat32Slot(4, accelerateLookAhead, 0.0)
def ControlConfigFBAddTargetSpeed(builder, targetSpeed): builder.PrependFloat32Slot(5, targetSpeed, 0.0)
def ControlConfigFBAddMaxSinuosity(builder, maxSinuosity): builder.PrependFloat32Slot(6, maxSinuosity, 0.0)
def ControlConfigFBAddSinuosityScale(builder, sinuosityScale): builder.PrependFloat32Slot(7, sinuosityScale, 0.0)
def ControlConfigFBAddSteeringMax(builder, steeringMax): builder.PrependFloat32Slot(10, steeringMax, 0.0)
def ControlConfigFBAddTargetSeparation(builder, targetSeparation): builder.PrependFloat32Slot(11, targetSeparation, 0.0)
def ControlConfigFBAddAggression(builder, aggression): builder.PrependFloat32Slot(12, aggression, 0.0)
def ControlConfigFBAddBrakeUntilTime(builder, brakeUntilTime): builder.PrependFloat32Slot(13, brakeUntilTime, 0.0)
def ControlConfigFBAddConstantAccelerate(builder, constantAccelerate): builder.PrependFloat32Slot(14, constantAccelerate, 0.0)
def ControlConfigFBAddSignedIntersectionConfigs(builder, signedIntersectionConfigs): builder.PrependUOffsetTRelativeSlot(27, flatbuffers.number_types.UOffsetTFlags.py_type(signedIntersectionConfigs), 0)
def ControlConfigFBStartSignedIntersectionConfigsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ControlConfigFBAddBrakeUntilEgoTimeToAgentS(builder, brakeUntilEgoTimeToAgentS): builder.PrependFloat32Slot(28, brakeUntilEgoTimeToAgentS, 0.0)
def ControlConfigFBAddInitialSteeringAngleRad(builder, initialSteeringAngleRad): builder.PrependFloat32Slot(29, initialSteeringAngleRad, 0.0)
def ControlConfigFBEnd(builder): return builder.EndObject()
