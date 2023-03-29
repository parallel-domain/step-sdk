# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class ReedSheppsCurveFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsReedSheppsCurveFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ReedSheppsCurveFB()
        x.Init(buf, n + offset)
        return x

    # ReedSheppsCurveFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ReedSheppsCurveFB
    def BaseWord(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

    # ReedSheppsCurveFB
    def Steps(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .ReedSheppsStepFB import ReedSheppsStepFB
            obj = ReedSheppsStepFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ReedSheppsCurveFB
    def StepsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ReedSheppsCurveFB
    def TurnRadiusM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ReedSheppsCurveFB
    def LengthM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def ReedSheppsCurveFBStart(builder): builder.StartObject(4)
def ReedSheppsCurveFBAddBaseWord(builder, baseWord): builder.PrependInt16Slot(0, baseWord, 0)
def ReedSheppsCurveFBAddSteps(builder, steps): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(steps), 0)
def ReedSheppsCurveFBStartStepsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ReedSheppsCurveFBAddTurnRadiusM(builder, turnRadiusM): builder.PrependFloat32Slot(2, turnRadiusM, 0.0)
def ReedSheppsCurveFBAddLengthM(builder, lengthM): builder.PrependFloat32Slot(3, lengthM, 0.0)
def ReedSheppsCurveFBEnd(builder): return builder.EndObject()