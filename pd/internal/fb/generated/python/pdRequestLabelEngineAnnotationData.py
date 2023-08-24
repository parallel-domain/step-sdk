# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdRequestLabelEngineAnnotationData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspdRequestLabelEngineAnnotationData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pdRequestLabelEngineAnnotationData()
        x.Init(buf, n + offset)
        return x

    # pdRequestLabelEngineAnnotationData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pdRequestLabelEngineAnnotationData
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # pdRequestLabelEngineAnnotationData
    def Label(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # pdRequestLabelEngineAnnotationData
    def Sensors(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # pdRequestLabelEngineAnnotationData
    def SensorsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # pdRequestLabelEngineAnnotationData
    def SceneName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

def pdRequestLabelEngineAnnotationDataStart(builder): builder.StartObject(4)
def pdRequestLabelEngineAnnotationDataAddTimestamp(builder, timestamp): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(timestamp), 0)
def pdRequestLabelEngineAnnotationDataAddLabel(builder, label): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(label), 0)
def pdRequestLabelEngineAnnotationDataAddSensors(builder, sensors): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(sensors), 0)
def pdRequestLabelEngineAnnotationDataStartSensorsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def pdRequestLabelEngineAnnotationDataAddSceneName(builder, sceneName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(sceneName), 0)
def pdRequestLabelEngineAnnotationDataEnd(builder): return builder.EndObject()