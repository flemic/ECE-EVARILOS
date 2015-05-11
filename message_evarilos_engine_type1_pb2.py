# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message_evarilos_engine_type1.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message_evarilos_engine_type1.proto',
  package='evarilos',
  serialized_pb='\n#message_evarilos_engine_type1.proto\x12\x08\x65varilos\"\xfc\x06\n\tece_type1\x12\x15\n\rtimestamp_utc\x18\x01 \x02(\x03\x12\x18\n\x10\x65xperiment_label\x18\x02 \x02(\t\x12\x37\n\tlocations\x18\x03 \x03(\x0b\x32$.evarilos.ece_type1.Evaluation_point\x12:\n\x08scenario\x18\x04 \x02(\x0b\x32(.evarilos.ece_type1.Scenario_description\x12(\n power_consumption_per_experiment\x18\x05 \x01(\x01\x12\x1c\n\rstore_metrics\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x13metrics_storage_URI\x18\x07 \x01(\t\x12 \n\x18metrics_storage_database\x18\x08 \x01(\t\x12\"\n\x1ametrics_storage_collection\x18\t \x01(\t\x1a\xbb\x02\n\x10\x45valuation_point\x12\x10\n\x08point_id\x18\x01 \x02(\x05\x12\x19\n\x11localized_node_id\x18\x02 \x01(\x05\x12\x19\n\x11true_coordinate_x\x18\x03 \x02(\x01\x12\x19\n\x11true_coordinate_y\x18\x04 \x02(\x01\x12\x19\n\x11true_coordinate_z\x18\x05 \x01(\x01\x12\x17\n\x0ftrue_room_label\x18\x06 \x01(\t\x12\x18\n\x10\x65st_coordinate_x\x18\x07 \x02(\x01\x12\x18\n\x10\x65st_coordinate_y\x18\x08 \x02(\x01\x12\x18\n\x10\x65st_coordinate_z\x18\t \x01(\x01\x12\x16\n\x0e\x65st_room_label\x18\n \x01(\t\x12\x0f\n\x07latency\x18\x0b \x01(\x01\x12\x19\n\x11power_consumption\x18\x0c \x01(\x01\x1a\xdf\x01\n\x14Scenario_description\x12\x15\n\rtestbed_label\x18\x01 \x02(\t\x12\x1b\n\x13testbed_description\x18\x02 \x02(\t\x12\x1e\n\x16\x65xperiment_description\x18\x03 \x02(\t\x12\x17\n\x0fsut_description\x18\x04 \x02(\t\x12\x1c\n\x14receiver_description\x18\x05 \x02(\t\x12\x1a\n\x12sender_description\x18\x06 \x02(\t\x12 \n\x18interference_description\x18\x07 \x02(\t')




_ECE_TYPE1_EVALUATION_POINT = _descriptor.Descriptor(
  name='Evaluation_point',
  full_name='evarilos.ece_type1.Evaluation_point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point_id', full_name='evarilos.ece_type1.Evaluation_point.point_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='localized_node_id', full_name='evarilos.ece_type1.Evaluation_point.localized_node_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='true_coordinate_x', full_name='evarilos.ece_type1.Evaluation_point.true_coordinate_x', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='true_coordinate_y', full_name='evarilos.ece_type1.Evaluation_point.true_coordinate_y', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='true_coordinate_z', full_name='evarilos.ece_type1.Evaluation_point.true_coordinate_z', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='true_room_label', full_name='evarilos.ece_type1.Evaluation_point.true_room_label', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='est_coordinate_x', full_name='evarilos.ece_type1.Evaluation_point.est_coordinate_x', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='est_coordinate_y', full_name='evarilos.ece_type1.Evaluation_point.est_coordinate_y', index=7,
      number=8, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='est_coordinate_z', full_name='evarilos.ece_type1.Evaluation_point.est_coordinate_z', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='est_room_label', full_name='evarilos.ece_type1.Evaluation_point.est_room_label', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latency', full_name='evarilos.ece_type1.Evaluation_point.latency', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power_consumption', full_name='evarilos.ece_type1.Evaluation_point.power_consumption', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=401,
  serialized_end=716,
)

_ECE_TYPE1_SCENARIO_DESCRIPTION = _descriptor.Descriptor(
  name='Scenario_description',
  full_name='evarilos.ece_type1.Scenario_description',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='testbed_label', full_name='evarilos.ece_type1.Scenario_description.testbed_label', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='testbed_description', full_name='evarilos.ece_type1.Scenario_description.testbed_description', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experiment_description', full_name='evarilos.ece_type1.Scenario_description.experiment_description', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sut_description', full_name='evarilos.ece_type1.Scenario_description.sut_description', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='receiver_description', full_name='evarilos.ece_type1.Scenario_description.receiver_description', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender_description', full_name='evarilos.ece_type1.Scenario_description.sender_description', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interference_description', full_name='evarilos.ece_type1.Scenario_description.interference_description', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=719,
  serialized_end=942,
)

_ECE_TYPE1 = _descriptor.Descriptor(
  name='ece_type1',
  full_name='evarilos.ece_type1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_utc', full_name='evarilos.ece_type1.timestamp_utc', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experiment_label', full_name='evarilos.ece_type1.experiment_label', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locations', full_name='evarilos.ece_type1.locations', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scenario', full_name='evarilos.ece_type1.scenario', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power_consumption_per_experiment', full_name='evarilos.ece_type1.power_consumption_per_experiment', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='store_metrics', full_name='evarilos.ece_type1.store_metrics', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metrics_storage_URI', full_name='evarilos.ece_type1.metrics_storage_URI', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metrics_storage_database', full_name='evarilos.ece_type1.metrics_storage_database', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metrics_storage_collection', full_name='evarilos.ece_type1.metrics_storage_collection', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ECE_TYPE1_EVALUATION_POINT, _ECE_TYPE1_SCENARIO_DESCRIPTION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=50,
  serialized_end=942,
)

_ECE_TYPE1_EVALUATION_POINT.containing_type = _ECE_TYPE1;
_ECE_TYPE1_SCENARIO_DESCRIPTION.containing_type = _ECE_TYPE1;
_ECE_TYPE1.fields_by_name['locations'].message_type = _ECE_TYPE1_EVALUATION_POINT
_ECE_TYPE1.fields_by_name['scenario'].message_type = _ECE_TYPE1_SCENARIO_DESCRIPTION
DESCRIPTOR.message_types_by_name['ece_type1'] = _ECE_TYPE1

class ece_type1(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Evaluation_point(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ECE_TYPE1_EVALUATION_POINT

    # @@protoc_insertion_point(class_scope:evarilos.ece_type1.Evaluation_point)

  class Scenario_description(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ECE_TYPE1_SCENARIO_DESCRIPTION

    # @@protoc_insertion_point(class_scope:evarilos.ece_type1.Scenario_description)
  DESCRIPTOR = _ECE_TYPE1

  # @@protoc_insertion_point(class_scope:evarilos.ece_type1)


# @@protoc_insertion_point(module_scope)
