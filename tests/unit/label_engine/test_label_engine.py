from pd.label_engine import LabelData


class TestLabelData:
    def test_data_as_annotation(self):
        """Annotation data object is properly parsed"""
        annotation_data = """
        {
         "geometry": {
          "primitives": [
           {
            "box_2d": {
             "min": {
              "x": 424,
              "y": 358
             },
             "max": {
              "x": 930,
              "y": 433
             }
            },
            "metadata": {
             "@type": "type.googleapis.com/pd.data.VisibilitySampleMetadata",
             "type": "eInstanceSample",
             "label": "",
             "instance_id": 0,
             "semantic_id": 4294967295,
             "mesh_id": 0,
             "submesh_index": 0,
             "bounds": {
              "min": {
               "x": 424,
               "y": 358
              },
              "max": {
               "x": 930,
               "y": 433
              }
             },
             "visible_bounds": {
              "min": {
               "x": 424,
               "y": 358
              },
              "max": {
               "x": 930,
               "y": 433
              }
             },
             "visibility": 0,
             "truncation": "NaN",
             "num_total_points": 0,
             "num_visible_points": 284,
             "num_on_screen_points": 0
            }
           }
          ]
         }
        }
        """
        label_data = LabelData(
            timestamp="001",
            label="test_annotation",
            sensor_id_and_name=(123, "testsensor"),
            data=annotation_data.encode(),
        )
        test_annotation = label_data.data_as_annotation
        assert len(test_annotation.geometry.primitives) == 1
        primitive = test_annotation.geometry.primitives[0]
        from pd.internal.proto.label_engine.generated.python.bounding_box_2d_pb2 import (
            VisibilitySampleMetadata,
            VisibilitySampleType,
        )

        visibility_sample_metadata = VisibilitySampleMetadata()
        primitive.metadata.Unpack(visibility_sample_metadata)
        assert visibility_sample_metadata.type == VisibilitySampleType.eInstanceSample
