# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class SimpleModuleOutputFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSimpleModuleOutputFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SimpleModuleOutputFB()
        x.Init(buf, n + offset)
        return x

    # SimpleModuleOutputFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SimpleModuleOutputFB
    def Distance(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # SimpleModuleOutputFB
    def TableA(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .SimpleModuleTableAFB import SimpleModuleTableAFB
            obj = SimpleModuleTableAFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # SimpleModuleOutputFB
    def TableALength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SimpleModuleOutputFB
    def TableB(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .SimpleModuleTableBFB import SimpleModuleTableBFB
            obj = SimpleModuleTableBFB()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def SimpleModuleOutputFBStart(builder): builder.StartObject(3)
def SimpleModuleOutputFBAddDistance(builder, distance): builder.PrependFloat32Slot(0, distance, 0.0)
def SimpleModuleOutputFBAddTableA(builder, tableA): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(tableA), 0)
def SimpleModuleOutputFBStartTableAVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def SimpleModuleOutputFBAddTableB(builder, tableB): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(tableB), 0)
def SimpleModuleOutputFBEnd(builder): return builder.EndObject()
