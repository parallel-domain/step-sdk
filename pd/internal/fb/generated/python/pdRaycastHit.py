# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdRaycastHit(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspdRaycastHit(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pdRaycastHit()
        x.Init(buf, n + offset)
        return x

    # pdRaycastHit
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pdRaycastHit
    def Locations(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 12
            from .pdFloat3 import pdFloat3
            obj = pdFloat3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # pdRaycastHit
    def LocationsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # pdRaycastHit
    def Normals(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 12
            from .pdFloat3 import pdFloat3
            obj = pdFloat3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # pdRaycastHit
    def NormalsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # pdRaycastHit
    def Flags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # pdRaycastHit
    def FlagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # pdRaycastHit
    def FlagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def pdRaycastHitStart(builder): builder.StartObject(3)
def pdRaycastHitAddLocations(builder, locations): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(locations), 0)
def pdRaycastHitStartLocationsVector(builder, numElems): return builder.StartVector(12, numElems, 4)
def pdRaycastHitAddNormals(builder, normals): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(normals), 0)
def pdRaycastHitStartNormalsVector(builder, numElems): return builder.StartVector(12, numElems, 4)
def pdRaycastHitAddFlags(builder, flags): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(flags), 0)
def pdRaycastHitStartFlagsVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def pdRaycastHitEnd(builder): return builder.EndObject()