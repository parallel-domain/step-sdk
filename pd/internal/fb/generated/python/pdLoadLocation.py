# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdLoadLocation(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspdLoadLocation(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pdLoadLocation()
        x.Init(buf, n + offset)
        return x

    # pdLoadLocation
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pdLoadLocation
    def LocationName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # pdLoadLocation
    def TimeOfDay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # pdLoadLocation
    def SceneName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

def pdLoadLocationStart(builder): builder.StartObject(3)
def pdLoadLocationAddLocationName(builder, locationName): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(locationName), 0)
def pdLoadLocationAddTimeOfDay(builder, timeOfDay): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(timeOfDay), 0)
def pdLoadLocationAddSceneName(builder, sceneName): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(sceneName), 0)
def pdLoadLocationEnd(builder): return builder.EndObject()
