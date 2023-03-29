# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class AliceLiDARModelFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAliceLiDARModelFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AliceLiDARModelFB()
        x.Init(buf, n + offset)
        return x

    # AliceLiDARModelFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AliceLiDARModelFB
    def NumberPoints(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # AliceLiDARModelFB
    def MinElevationAngle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AliceLiDARModelFB
    def MaxElevationAngle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AliceLiDARModelFB
    def MinDenseElevationAngle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AliceLiDARModelFB
    def MaxDenseElevationAngle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AliceLiDARModelFB
    def MinAzimuthAngle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AliceLiDARModelFB
    def MaxAzimuthAngle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AliceLiDARModelFB
    def SparseRadianSpacing(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AliceLiDARModelFB
    def DenseRadianSpacing(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AliceLiDARModelFB
    def HorizontalSpacing(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def AliceLiDARModelFBStart(builder): builder.StartObject(10)
def AliceLiDARModelFBAddNumberPoints(builder, numberPoints): builder.PrependInt32Slot(0, numberPoints, 0)
def AliceLiDARModelFBAddMinElevationAngle(builder, minElevationAngle): builder.PrependFloat32Slot(1, minElevationAngle, 0.0)
def AliceLiDARModelFBAddMaxElevationAngle(builder, maxElevationAngle): builder.PrependFloat32Slot(2, maxElevationAngle, 0.0)
def AliceLiDARModelFBAddMinDenseElevationAngle(builder, minDenseElevationAngle): builder.PrependFloat32Slot(3, minDenseElevationAngle, 0.0)
def AliceLiDARModelFBAddMaxDenseElevationAngle(builder, maxDenseElevationAngle): builder.PrependFloat32Slot(4, maxDenseElevationAngle, 0.0)
def AliceLiDARModelFBAddMinAzimuthAngle(builder, minAzimuthAngle): builder.PrependFloat32Slot(5, minAzimuthAngle, 0.0)
def AliceLiDARModelFBAddMaxAzimuthAngle(builder, maxAzimuthAngle): builder.PrependFloat32Slot(6, maxAzimuthAngle, 0.0)
def AliceLiDARModelFBAddSparseRadianSpacing(builder, sparseRadianSpacing): builder.PrependFloat32Slot(7, sparseRadianSpacing, 0.0)
def AliceLiDARModelFBAddDenseRadianSpacing(builder, denseRadianSpacing): builder.PrependFloat32Slot(8, denseRadianSpacing, 0.0)
def AliceLiDARModelFBAddHorizontalSpacing(builder, horizontalSpacing): builder.PrependFloat32Slot(9, horizontalSpacing, 0.0)
def AliceLiDARModelFBEnd(builder): return builder.EndObject()