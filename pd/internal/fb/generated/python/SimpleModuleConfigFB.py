# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class SimpleModuleConfigFB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSimpleModuleConfigFB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SimpleModuleConfigFB()
        x.Init(buf, n + offset)
        return x

    # SimpleModuleConfigFB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SimpleModuleConfigFB
    def Speed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def SimpleModuleConfigFBStart(builder): builder.StartObject(1)
def SimpleModuleConfigFBAddSpeed(builder, speed): builder.PrependFloat32Slot(0, speed, 0.0)
def SimpleModuleConfigFBEnd(builder): return builder.EndObject()
