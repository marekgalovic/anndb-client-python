# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anndb/search.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='anndb/search.proto',
  package='anndb_pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12\x61nndb/search.proto\x12\x08\x61nndb_pb\"=\n\rSearchRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\x0c\x12\r\n\x05query\x18\x02 \x03(\x02\x12\t\n\x01k\x18\x03 \x01(\r\"^\n\x17SearchPartitionsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\x0c\x12\x15\n\rpartition_ids\x18\x02 \x03(\x0c\x12\r\n\x05query\x18\x03 \x03(\x02\x12\t\n\x01k\x18\x04 \x01(\r\"\x9a\x01\n\x10SearchResultItem\x12\n\n\x02id\x18\x01 \x01(\x04\x12:\n\x08metadata\x18\x02 \x03(\x0b\x32(.anndb_pb.SearchResultItem.MetadataEntry\x12\r\n\x05score\x18\x03 \x01(\x02\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x9e\x01\n\x06Search\x12?\n\x06Search\x12\x17.anndb_pb.SearchRequest\x1a\x1a.anndb_pb.SearchResultItem0\x01\x12S\n\x10SearchPartitions\x12!.anndb_pb.SearchPartitionsRequest\x1a\x1a.anndb_pb.SearchResultItem0\x01\x62\x06proto3')
)




_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='anndb_pb.SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='anndb_pb.SearchRequest.dataset_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='anndb_pb.SearchRequest.query', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k', full_name='anndb_pb.SearchRequest.k', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=32,
  serialized_end=93,
)


_SEARCHPARTITIONSREQUEST = _descriptor.Descriptor(
  name='SearchPartitionsRequest',
  full_name='anndb_pb.SearchPartitionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='anndb_pb.SearchPartitionsRequest.dataset_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partition_ids', full_name='anndb_pb.SearchPartitionsRequest.partition_ids', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='anndb_pb.SearchPartitionsRequest.query', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k', full_name='anndb_pb.SearchPartitionsRequest.k', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=95,
  serialized_end=189,
)


_SEARCHRESULTITEM_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='anndb_pb.SearchResultItem.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='anndb_pb.SearchResultItem.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='anndb_pb.SearchResultItem.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=346,
)

_SEARCHRESULTITEM = _descriptor.Descriptor(
  name='SearchResultItem',
  full_name='anndb_pb.SearchResultItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='anndb_pb.SearchResultItem.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='anndb_pb.SearchResultItem.metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='anndb_pb.SearchResultItem.score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHRESULTITEM_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=346,
)

_SEARCHRESULTITEM_METADATAENTRY.containing_type = _SEARCHRESULTITEM
_SEARCHRESULTITEM.fields_by_name['metadata'].message_type = _SEARCHRESULTITEM_METADATAENTRY
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchPartitionsRequest'] = _SEARCHPARTITIONSREQUEST
DESCRIPTOR.message_types_by_name['SearchResultItem'] = _SEARCHRESULTITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREQUEST,
  __module__ = 'anndb.search_pb2'
  # @@protoc_insertion_point(class_scope:anndb_pb.SearchRequest)
  ))
_sym_db.RegisterMessage(SearchRequest)

SearchPartitionsRequest = _reflection.GeneratedProtocolMessageType('SearchPartitionsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHPARTITIONSREQUEST,
  __module__ = 'anndb.search_pb2'
  # @@protoc_insertion_point(class_scope:anndb_pb.SearchPartitionsRequest)
  ))
_sym_db.RegisterMessage(SearchPartitionsRequest)

SearchResultItem = _reflection.GeneratedProtocolMessageType('SearchResultItem', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _SEARCHRESULTITEM_METADATAENTRY,
    __module__ = 'anndb.search_pb2'
    # @@protoc_insertion_point(class_scope:anndb_pb.SearchResultItem.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _SEARCHRESULTITEM,
  __module__ = 'anndb.search_pb2'
  # @@protoc_insertion_point(class_scope:anndb_pb.SearchResultItem)
  ))
_sym_db.RegisterMessage(SearchResultItem)
_sym_db.RegisterMessage(SearchResultItem.MetadataEntry)


_SEARCHRESULTITEM_METADATAENTRY._options = None

_SEARCH = _descriptor.ServiceDescriptor(
  name='Search',
  full_name='anndb_pb.Search',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=349,
  serialized_end=507,
  methods=[
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='anndb_pb.Search.Search',
    index=0,
    containing_service=None,
    input_type=_SEARCHREQUEST,
    output_type=_SEARCHRESULTITEM,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SearchPartitions',
    full_name='anndb_pb.Search.SearchPartitions',
    index=1,
    containing_service=None,
    input_type=_SEARCHPARTITIONSREQUEST,
    output_type=_SEARCHRESULTITEM,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEARCH)

DESCRIPTOR.services_by_name['Search'] = _SEARCH

# @@protoc_insertion_point(module_scope)
