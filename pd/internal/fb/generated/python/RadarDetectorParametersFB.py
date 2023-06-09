# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class RadarDetectorParametersFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRadarDetectorParametersFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RadarDetectorParametersFB()
        x.Init(buf, n + offset)
        return x

    # RadarDetectorParametersFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RadarDetectorParametersFB
    def DetectorType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # RadarDetectorParametersFB
    def DetectorConstantGain(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # RadarDetectorParametersFB
    def DetectorRadiometricGain(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # RadarDetectorParametersFB
    def DetectorRadiometricDecay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def RadarDetectorParametersFBStart(builder): builder.StartObject(4)
def RadarDetectorParametersFBAddDetectorType(builder, detectorType): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(detectorType), 0)
def RadarDetectorParametersFBAddDetectorConstantGain(builder, detectorConstantGain): builder.PrependFloat32Slot(1, detectorConstantGain, 0.0)
def RadarDetectorParametersFBAddDetectorRadiometricGain(builder, detectorRadiometricGain): builder.PrependFloat32Slot(2, detectorRadiometricGain, 0.0)
def RadarDetectorParametersFBAddDetectorRadiometricDecay(builder, detectorRadiometricDecay): builder.PrependFloat32Slot(3, detectorRadiometricDecay, 0.0)
def RadarDetectorParametersFBEnd(builder): return builder.EndObject()
