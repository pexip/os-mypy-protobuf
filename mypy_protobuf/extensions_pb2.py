# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mypy_protobuf/extensions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1emypy_protobuf/extensions.proto\x12\rmypy_protobuf\x1a google/protobuf/descriptor.proto:1\n\x08\x63\x61sttype\x12\x1d.google.protobuf.FieldOptions\x18\xe0\xd4\x03 \x01(\t:0\n\x07keytype\x12\x1d.google.protobuf.FieldOptions\x18\xe2\xd4\x03 \x01(\t:2\n\tvaluetype\x12\x1d.google.protobuf.FieldOptions\x18\xe3\xd4\x03 \x01(\t')


CASTTYPE_FIELD_NUMBER = 60000
casttype = DESCRIPTOR.extensions_by_name['casttype']
KEYTYPE_FIELD_NUMBER = 60002
keytype = DESCRIPTOR.extensions_by_name['keytype']
VALUETYPE_FIELD_NUMBER = 60003
valuetype = DESCRIPTOR.extensions_by_name['valuetype']

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(casttype)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(keytype)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(valuetype)

  DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
