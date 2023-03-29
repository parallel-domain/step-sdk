# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class RadarEnergyParametersFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRadarEnergyParametersFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RadarEnergyParametersFB()
        x.Init(buf, n + offset)
        return x

    # RadarEnergyParametersFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RadarEnergyParametersFB
    def NominalGain(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # RadarEnergyParametersFB
    def GainJitterStd(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # RadarEnergyParametersFB
    def RadiometricCoefficient(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # RadarEnergyParametersFB
    def BeamPatternFilePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # RadarEnergyParametersFB
    def EnableBeamPattern(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

def RadarEnergyParametersFBStart(builder): builder.StartObject(5)
def RadarEnergyParametersFBAddNominalGain(builder, nominalGain): builder.PrependFloat32Slot(0, nominalGain, 0.0)
def RadarEnergyParametersFBAddGainJitterStd(builder, gainJitterStd): builder.PrependFloat32Slot(1, gainJitterStd, 0.0)
def RadarEnergyParametersFBAddRadiometricCoefficient(builder, radiometricCoefficient): builder.PrependFloat32Slot(2, radiometricCoefficient, 0.0)
def RadarEnergyParametersFBAddBeamPatternFilePath(builder, beamPatternFilePath): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(beamPatternFilePath), 0)
def RadarEnergyParametersFBAddEnableBeamPattern(builder, enableBeamPattern): builder.PrependBoolSlot(4, enableBeamPattern, 0)
def RadarEnergyParametersFBEnd(builder): return builder.EndObject()
