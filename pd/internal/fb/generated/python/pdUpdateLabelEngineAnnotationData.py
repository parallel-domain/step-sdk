# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class pdUpdateLabelEngineAnnotationData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAspdUpdateLabelEngineAnnotationData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = pdUpdateLabelEngineAnnotationData()
        x.Init(buf, n + offset)
        return x

    # pdUpdateLabelEngineAnnotationData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # pdUpdateLabelEngineAnnotationData
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # pdUpdateLabelEngineAnnotationData
    def Sensor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # pdUpdateLabelEngineAnnotationData
    def Label(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

    # pdUpdateLabelEngineAnnotationData
    def DataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # pdUpdateLabelEngineAnnotationData
    def LabelData(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # pdUpdateLabelEngineAnnotationData
    def LabelDataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # pdUpdateLabelEngineAnnotationData
    def LabelDataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # pdUpdateLabelEngineAnnotationData
    def SceneName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return bytes()

def pdUpdateLabelEngineAnnotationDataStart(builder): builder.StartObject(6)
def pdUpdateLabelEngineAnnotationDataAddTimestamp(builder, timestamp): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(timestamp), 0)
def pdUpdateLabelEngineAnnotationDataAddSensor(builder, sensor): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(sensor), 0)
def pdUpdateLabelEngineAnnotationDataAddLabel(builder, label): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(label), 0)
def pdUpdateLabelEngineAnnotationDataAddDataType(builder, dataType): builder.PrependInt32Slot(3, dataType, 0)
def pdUpdateLabelEngineAnnotationDataAddLabelData(builder, labelData): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(labelData), 0)
def pdUpdateLabelEngineAnnotationDataStartLabelDataVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def pdUpdateLabelEngineAnnotationDataAddSceneName(builder, sceneName): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(sceneName), 0)
def pdUpdateLabelEngineAnnotationDataEnd(builder): return builder.EndObject()