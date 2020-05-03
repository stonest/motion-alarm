# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alarm.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='alarm.proto',
  package='alarm',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0b\x61larm.proto\x12\x05\x61larm\".\n\x05\x41larm\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03\x64\x61y\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\t\"}\n\x0e\x41\x63tionResponse\x12,\n\x06status\x18\x02 \x01(\x0e\x32\x1c.alarm.ActionResponse.Status\x12\x1c\n\x06\x61larms\x18\x03 \x03(\x0b\x32\x0c.alarm.Alarm\"\x1f\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\"\x12\n\x10ListAlarmsParams2\xf0\x01\n\nAlarmStore\x12\x34\n\x0b\x44\x65leteAlarm\x12\x0c.alarm.Alarm\x1a\x15.alarm.ActionResponse\"\x00\x12\x34\n\x0bUpdateAlarm\x12\x0c.alarm.Alarm\x1a\x15.alarm.ActionResponse\"\x00\x12@\n\nListAlarms\x12\x17.alarm.ListAlarmsParams\x1a\x15.alarm.ActionResponse\"\x00\x30\x01\x12\x34\n\x0b\x43reateAlarm\x12\x0c.alarm.Alarm\x1a\x15.alarm.ActionResponse\"\x00\x62\x06proto3'
)



_ACTIONRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='alarm.ActionResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=164,
  serialized_end=195,
)
_sym_db.RegisterEnumDescriptor(_ACTIONRESPONSE_STATUS)


_ALARM = _descriptor.Descriptor(
  name='Alarm',
  full_name='alarm.Alarm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='alarm.Alarm.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='alarm.Alarm.day', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='alarm.Alarm.time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=68,
)


_ACTIONRESPONSE = _descriptor.Descriptor(
  name='ActionResponse',
  full_name='alarm.ActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='alarm.ActionResponse.status', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alarms', full_name='alarm.ActionResponse.alarms', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACTIONRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=195,
)


_LISTALARMSPARAMS = _descriptor.Descriptor(
  name='ListAlarmsParams',
  full_name='alarm.ListAlarmsParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=215,
)

_ACTIONRESPONSE.fields_by_name['status'].enum_type = _ACTIONRESPONSE_STATUS
_ACTIONRESPONSE.fields_by_name['alarms'].message_type = _ALARM
_ACTIONRESPONSE_STATUS.containing_type = _ACTIONRESPONSE
DESCRIPTOR.message_types_by_name['Alarm'] = _ALARM
DESCRIPTOR.message_types_by_name['ActionResponse'] = _ACTIONRESPONSE
DESCRIPTOR.message_types_by_name['ListAlarmsParams'] = _LISTALARMSPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Alarm = _reflection.GeneratedProtocolMessageType('Alarm', (_message.Message,), {
  'DESCRIPTOR' : _ALARM,
  '__module__' : 'alarm_pb2'
  # @@protoc_insertion_point(class_scope:alarm.Alarm)
  })
_sym_db.RegisterMessage(Alarm)

ActionResponse = _reflection.GeneratedProtocolMessageType('ActionResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONRESPONSE,
  '__module__' : 'alarm_pb2'
  # @@protoc_insertion_point(class_scope:alarm.ActionResponse)
  })
_sym_db.RegisterMessage(ActionResponse)

ListAlarmsParams = _reflection.GeneratedProtocolMessageType('ListAlarmsParams', (_message.Message,), {
  'DESCRIPTOR' : _LISTALARMSPARAMS,
  '__module__' : 'alarm_pb2'
  # @@protoc_insertion_point(class_scope:alarm.ListAlarmsParams)
  })
_sym_db.RegisterMessage(ListAlarmsParams)



_ALARMSTORE = _descriptor.ServiceDescriptor(
  name='AlarmStore',
  full_name='alarm.AlarmStore',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=218,
  serialized_end=458,
  methods=[
  _descriptor.MethodDescriptor(
    name='DeleteAlarm',
    full_name='alarm.AlarmStore.DeleteAlarm',
    index=0,
    containing_service=None,
    input_type=_ALARM,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAlarm',
    full_name='alarm.AlarmStore.UpdateAlarm',
    index=1,
    containing_service=None,
    input_type=_ALARM,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListAlarms',
    full_name='alarm.AlarmStore.ListAlarms',
    index=2,
    containing_service=None,
    input_type=_LISTALARMSPARAMS,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateAlarm',
    full_name='alarm.AlarmStore.CreateAlarm',
    index=3,
    containing_service=None,
    input_type=_ALARM,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ALARMSTORE)

DESCRIPTOR.services_by_name['AlarmStore'] = _ALARMSTORE

# @@protoc_insertion_point(module_scope)
