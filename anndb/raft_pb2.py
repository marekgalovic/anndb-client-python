# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import core_pb2 as core__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='raft.proto',
  package='anndb_pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\nraft.proto\x12\x08\x61nndb_pb\x1a\ncore.proto\"1\n\x0bRaftMessage\x12\x10\n\x08group_id\x18\x01 \x01(\x0c\x12\x10\n\x08messages\x18\x02 \x03(\x0c\x32I\n\rRaftTransport\x12\x38\n\x07Receive\x12\x15.anndb_pb.RaftMessage\x1a\x16.anndb_pb.EmptyMessageb\x06proto3'
  ,
  dependencies=[core__pb2.DESCRIPTOR,])




_RAFTMESSAGE = _descriptor.Descriptor(
  name='RaftMessage',
  full_name='anndb_pb.RaftMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='anndb_pb.RaftMessage.group_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messages', full_name='anndb_pb.RaftMessage.messages', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=36,
  serialized_end=85,
)

DESCRIPTOR.message_types_by_name['RaftMessage'] = _RAFTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RaftMessage = _reflection.GeneratedProtocolMessageType('RaftMessage', (_message.Message,), {
  'DESCRIPTOR' : _RAFTMESSAGE,
  '__module__' : 'raft_pb2'
  # @@protoc_insertion_point(class_scope:anndb_pb.RaftMessage)
  })
_sym_db.RegisterMessage(RaftMessage)



_RAFTTRANSPORT = _descriptor.ServiceDescriptor(
  name='RaftTransport',
  full_name='anndb_pb.RaftTransport',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=87,
  serialized_end=160,
  methods=[
  _descriptor.MethodDescriptor(
    name='Receive',
    full_name='anndb_pb.RaftTransport.Receive',
    index=0,
    containing_service=None,
    input_type=_RAFTMESSAGE,
    output_type=core__pb2._EMPTYMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RAFTTRANSPORT)

DESCRIPTOR.services_by_name['RaftTransport'] = _RAFTTRANSPORT

# @@protoc_insertion_point(module_scope)