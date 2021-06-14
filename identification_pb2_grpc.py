
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import identification_pb2 as identification__pb2


class IdentiteStub(object):


  def __init__(self, channel):

    self.Identifie = channel.unary_unary(
        '/Identite/Identifie',
        request_serializer=identification__pb2.IdentificationRequest.SerializeToString,
        response_deserializer=identification__pb2.IdentificationReply.FromString,
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
          request_deserializer=identification__pb2.IdentificationRequest.FromString,
          response_serializer=identification__pb2.IdentificationReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Identite', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
