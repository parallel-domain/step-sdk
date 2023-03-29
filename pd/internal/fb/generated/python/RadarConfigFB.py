# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class RadarConfigFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRadarConfigFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RadarConfigFB()
        x.Init(buf, n + offset)
        return x

    # RadarConfigFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RadarConfigFB
    def BasicParameters(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .RadarBasicParametersFB import RadarBasicParametersFB
            obj = RadarBasicParametersFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # RadarConfigFB
    def EnergyParameters(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .RadarEnergyParametersFB import RadarEnergyParametersFB
            obj = RadarEnergyParametersFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # RadarConfigFB
    def NoiseParameters(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .RadarNoiseParametersFB import RadarNoiseParametersFB
            obj = RadarNoiseParametersFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # RadarConfigFB
    def DetectorParameters(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .RadarDetectorParametersFB import RadarDetectorParametersFB
            obj = RadarDetectorParametersFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def RadarConfigFBStart(builder): builder.StartObject(4)
def RadarConfigFBAddBasicParameters(builder, basicParameters): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(basicParameters), 0)
def RadarConfigFBAddEnergyParameters(builder, energyParameters): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(energyParameters), 0)
def RadarConfigFBAddNoiseParameters(builder, noiseParameters): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(noiseParameters), 0)
def RadarConfigFBAddDetectorParameters(builder, detectorParameters): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(detectorParameters), 0)
def RadarConfigFBEnd(builder): return builder.EndObject()
