# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anndb/core.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='anndb/core.proto',
  package='anndb_pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x61nndb/core.proto\x12\x08\x61nndb_pb\"\x0e\n\x0c\x45mptyMessage\"\x19\n\x0bUUIDRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\x62\x06proto3')
)




_EMPTYMESSAGE = _descriptor.Descriptor(
  name='EmptyMessage',
  full_name='anndb_pb.EmptyMessage',
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
  serialized_start=30,
  serialized_end=44,
)


_UUIDREQUEST = _descriptor.Descriptor(
  name='UUIDRequest',
  full_name='anndb_pb.UUIDRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='anndb_pb.UUIDRequest.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=46,
  serialized_end=71,
)

DESCRIPTOR.message_types_by_name['EmptyMessage'] = _EMPTYMESSAGE
DESCRIPTOR.message_types_by_name['UUIDRequest'] = _UUIDREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyMessage = _reflection.GeneratedProtocolMessageType('EmptyMessage', (_message.Message,), dict(
  DESCRIPTOR = _EMPTYMESSAGE,
  __module__ = 'anndb.core_pb2'
  # @@protoc_insertion_point(class_scope:anndb_pb.EmptyMessage)
  ))
_sym_db.RegisterMessage(EmptyMessage)

UUIDRequest = _reflection.GeneratedProtocolMessageType('UUIDRequest', (_message.Message,), dict(
  DESCRIPTOR = _UUIDREQUEST,
  __module__ = 'anndb.core_pb2'
  # @@protoc_insertion_point(class_scope:anndb_pb.UUIDRequest)
  ))
_sym_db.RegisterMessage(UUIDRequest)


# @@protoc_insertion_point(module_scope)
