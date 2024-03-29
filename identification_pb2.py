import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='identification.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x14identification.proto\"7\n\x15IdentificationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"&\n\x13IdentificationReply\x12\x0f\n\x07message\x18\x01 \x01(\x05\x32G\n\x08Identite\x12;\n\tIdentifie\x12\x16.IdentificationRequest\x1a\x14.IdentificationReply\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IDENTIFICATIONREQUEST = _descriptor.Descriptor(
  name='IdentificationRequest',
  full_name='IdentificationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='IdentificationRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='IdentificationRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=79,
)


_IDENTIFICATIONREPLY = _descriptor.Descriptor(
  name='IdentificationReply',
  full_name='IdentificationReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='IdentificationReply.message', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=119,
)

DESCRIPTOR.message_types_by_name['IdentificationRequest'] = _IDENTIFICATIONREQUEST
DESCRIPTOR.message_types_by_name['IdentificationReply'] = _IDENTIFICATIONREPLY

IdentificationRequest = _reflection.GeneratedProtocolMessageType('IdentificationRequest', (_message.Message,), dict(
  DESCRIPTOR = _IDENTIFICATIONREQUEST,
  __module__ = 'identification_pb2'
  ))
_sym_db.RegisterMessage(IdentificationRequest)

IdentificationReply = _reflection.GeneratedProtocolMessageType('IdentificationReply', (_message.Message,), dict(
  DESCRIPTOR = _IDENTIFICATIONREPLY,
  __module__ = 'identification_pb2'
  ))
_sym_db.RegisterMessage(IdentificationReply)


try:
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class IdentiteStub(object):

    def __init__(self, channel):

      self.Identifie = channel.unary_unary(
          '/Identite/Identifie',
          request_serializer=IdentificationRequest.SerializeToString,
          response_deserializer=IdentificationReply.FromString,
          )


  class IdentiteServicer(object):


    def Identifie(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_IdentiteServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Identifie': grpc.unary_unary_rpc_method_handler(
            servicer.Identifie,
            request_deserializer=IdentificationRequest.FromString,
            response_serializer=IdentificationReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Identite', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaIdentiteServicer(object):

    def Identifie(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaIdentiteStub(object):

    def Identifie(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    Identifie.future = None


  def beta_create_Identite_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):

    request_deserializers = {
      ('Identite', 'Identifie'): IdentificationRequest.FromString,
    }
    response_serializers = {
      ('Identite', 'Identifie'): IdentificationReply.SerializeToString,
    }
    method_implementations = {
      ('Identite', 'Identifie'): face_utilities.unary_unary_inline(servicer.Identifie),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Identite_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):

    request_serializers = {
      ('Identite', 'Identifie'): IdentificationRequest.SerializeToString,
    }
    response_deserializers = {
      ('Identite', 'Identifie'): IdentificationReply.FromString,
    }
    cardinalities = {
      'Identifie': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Identite', cardinalities, options=stub_options)
except ImportError:
  pass

