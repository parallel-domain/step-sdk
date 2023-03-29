# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class RadarBasicParametersFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRadarBasicParametersFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RadarBasicParametersFB()
        x.Init(buf, n + offset)
        return x

    # RadarBasicParametersFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RadarBasicParametersFB
    def MaxRange(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # RadarBasicParametersFB
    def RangeResolution(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # RadarBasicParametersFB
    def MaxDoppler(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # RadarBasicParametersFB
    def DopplerResolution(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # RadarBasicParametersFB
    def AzimuthFov(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # RadarBasicParametersFB
    def AzimuthResolution(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # RadarBasicParametersFB
    def ElevationFov(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # RadarBasicParametersFB
    def ElevationResolution(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # RadarBasicParametersFB
    def RadarOutput2d(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # RadarBasicParametersFB
    def UseRandomRaycast(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

    # RadarBasicParametersFB
    def NumberRaysPerFrame(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def RadarBasicParametersFBStart(builder): builder.StartObject(11)
def RadarBasicParametersFBAddMaxRange(builder, maxRange): builder.PrependFloat32Slot(0, maxRange, 0.0)
def RadarBasicParametersFBAddRangeResolution(builder, rangeResolution): builder.PrependFloat32Slot(1, rangeResolution, 0.0)
def RadarBasicParametersFBAddMaxDoppler(builder, maxDoppler): builder.PrependFloat32Slot(2, maxDoppler, 0.0)
def RadarBasicParametersFBAddDopplerResolution(builder, dopplerResolution): builder.PrependFloat32Slot(3, dopplerResolution, 0.0)
def RadarBasicParametersFBAddAzimuthFov(builder, azimuthFov): builder.PrependFloat32Slot(4, azimuthFov, 0.0)
def RadarBasicParametersFBAddAzimuthResolution(builder, azimuthResolution): builder.PrependFloat32Slot(5, azimuthResolution, 0.0)
def RadarBasicParametersFBAddElevationFov(builder, elevationFov): builder.PrependFloat32Slot(6, elevationFov, 0.0)
def RadarBasicParametersFBAddElevationResolution(builder, elevationResolution): builder.PrependFloat32Slot(7, elevationResolution, 0.0)
def RadarBasicParametersFBAddRadarOutput2d(builder, radarOutput2d): builder.PrependBoolSlot(8, radarOutput2d, 0)
def RadarBasicParametersFBAddUseRandomRaycast(builder, useRandomRaycast): builder.PrependBoolSlot(9, useRandomRaycast, 0)
def RadarBasicParametersFBAddNumberRaysPerFrame(builder, numberRaysPerFrame): builder.PrependInt32Slot(10, numberRaysPerFrame, 0)
def RadarBasicParametersFBEnd(builder): return builder.EndObject()
