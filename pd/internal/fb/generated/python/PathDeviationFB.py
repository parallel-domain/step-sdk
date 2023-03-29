# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class PathDeviationFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPathDeviationFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PathDeviationFB()
        x.Init(buf, n + offset)
        return x

    # PathDeviationFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PathDeviationFB
    def HeadingError(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # PathDeviationFB
    def CrosstrackError(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def PathDeviationFBStart(builder): builder.StartObject(2)
def PathDeviationFBAddHeadingError(builder, headingError): builder.PrependFloat32Slot(0, headingError, 0.0)
def PathDeviationFBAddCrosstrackError(builder, crosstrackError): builder.PrependFloat32Slot(1, crosstrackError, 0.0)
def PathDeviationFBEnd(builder): return builder.EndObject()
