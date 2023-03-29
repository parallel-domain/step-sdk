# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class NavRouteSegmentFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsNavRouteSegmentFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NavRouteSegmentFB()
        x.Init(buf, n + offset)
        return x

    # NavRouteSegmentFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NavRouteSegmentFB
    def StartDistanceM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # NavRouteSegmentFB
    def StartHeadingOffsetRad(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # NavRouteSegmentFB
    def EndDistanceM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # NavRouteSegmentFB
    def EndHeadingOffsetRad(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

# /// lane segments in this route segment. 
    # NavRouteSegmentFB
    def LaneSegments(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # NavRouteSegmentFB
    def LaneSegmentsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # NavRouteSegmentFB
    def LaneSegmentsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

# /// Set to true to use the target speed
    # NavRouteSegmentFB
    def UseTargetSpeed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos)
        return 0

# /// target speed along this segment
    # NavRouteSegmentFB
    def TargetSpeedMps(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

# /// Maneuver to perform at the start of this segment.
    # NavRouteSegmentFB
    def StartManeuver(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

# /// start lateral offset in meters.
    # NavRouteSegmentFB
    def StartLateralOffsetM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

# /// end lateral offset in meters.
    # NavRouteSegmentFB
    def EndLateralOffsetM(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def NavRouteSegmentFBStart(builder): builder.StartObject(10)
def NavRouteSegmentFBAddStartDistanceM(builder, startDistanceM): builder.PrependFloat32Slot(0, startDistanceM, 0.0)
def NavRouteSegmentFBAddStartHeadingOffsetRad(builder, startHeadingOffsetRad): builder.PrependFloat32Slot(1, startHeadingOffsetRad, 0.0)
def NavRouteSegmentFBAddEndDistanceM(builder, endDistanceM): builder.PrependFloat32Slot(2, endDistanceM, 0.0)
def NavRouteSegmentFBAddEndHeadingOffsetRad(builder, endHeadingOffsetRad): builder.PrependFloat32Slot(3, endHeadingOffsetRad, 0.0)
def NavRouteSegmentFBAddLaneSegments(builder, laneSegments): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(laneSegments), 0)
def NavRouteSegmentFBStartLaneSegmentsVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def NavRouteSegmentFBAddUseTargetSpeed(builder, useTargetSpeed): builder.PrependBoolSlot(5, useTargetSpeed, 0)
def NavRouteSegmentFBAddTargetSpeedMps(builder, targetSpeedMps): builder.PrependFloat32Slot(6, targetSpeedMps, 0.0)
def NavRouteSegmentFBAddStartManeuver(builder, startManeuver): builder.PrependInt8Slot(7, startManeuver, 0)
def NavRouteSegmentFBAddStartLateralOffsetM(builder, startLateralOffsetM): builder.PrependFloat32Slot(8, startLateralOffsetM, 0.0)
def NavRouteSegmentFBAddEndLateralOffsetM(builder, endLateralOffsetM): builder.PrependFloat32Slot(9, endLateralOffsetM, 0.0)
def NavRouteSegmentFBEnd(builder): return builder.EndObject()
