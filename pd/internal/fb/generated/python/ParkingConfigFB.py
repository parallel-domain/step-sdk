# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class ParkingConfigFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsParkingConfigFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ParkingConfigFB()
        x.Init(buf, n + offset)
        return x

    # ParkingConfigFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ParkingConfigFB
    def Angle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ParkingConfigFB
    def LotParkingDelineationType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ParkingConfigFB
    def StreetParkingDelineationType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ParkingConfigFB
    def StreetParkingAngleZeroOverride(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ParkingConfigFB
    def DelineationColor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = o + self._tab.Pos
            from .float3_t import float3_t
            obj = float3_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ParkingConfigFB
    def DelineationWearAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # ParkingConfigFB
    def ParkingSpaceMaterial(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ParkingConfigFB
    def ParkingSpaceTint(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = o + self._tab.Pos
            from .float3_t import float3_t
            obj = float3_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ParkingConfigFB
    def ParkingSpaceGrungeAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def ParkingConfigFBStart(builder): builder.StartObject(9)
def ParkingConfigFBAddAngle(builder, angle): builder.PrependInt32Slot(0, angle, 0)
def ParkingConfigFBAddLotParkingDelineationType(builder, lotParkingDelineationType): builder.PrependInt32Slot(1, lotParkingDelineationType, 0)
def ParkingConfigFBAddStreetParkingDelineationType(builder, streetParkingDelineationType): builder.PrependInt32Slot(2, streetParkingDelineationType, 0)
def ParkingConfigFBAddStreetParkingAngleZeroOverride(builder, streetParkingAngleZeroOverride): builder.PrependInt32Slot(3, streetParkingAngleZeroOverride, 0)
def ParkingConfigFBAddDelineationColor(builder, delineationColor): builder.PrependStructSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(delineationColor), 0)
def ParkingConfigFBAddDelineationWearAmount(builder, delineationWearAmount): builder.PrependFloat32Slot(5, delineationWearAmount, 0.0)
def ParkingConfigFBAddParkingSpaceMaterial(builder, parkingSpaceMaterial): builder.PrependInt32Slot(6, parkingSpaceMaterial, 0)
def ParkingConfigFBAddParkingSpaceTint(builder, parkingSpaceTint): builder.PrependStructSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(parkingSpaceTint), 0)
def ParkingConfigFBAddParkingSpaceGrungeAmount(builder, parkingSpaceGrungeAmount): builder.PrependFloat32Slot(8, parkingSpaceGrungeAmount, 0.0)
def ParkingConfigFBEnd(builder): return builder.EndObject()
