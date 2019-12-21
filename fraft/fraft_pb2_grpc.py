# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import fraft_pb2 as fraft__pb2


class fRaftStub(object):
  """fRaft gRPC implementation
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RequestVote = channel.unary_unary(
        '/fRaft/RequestVote',
        request_serializer=fraft__pb2.VoteRequest.SerializeToString,
        response_deserializer=fraft__pb2.Ack.FromString,
        )
    self.AppendEntries = channel.unary_unary(
        '/fRaft/AppendEntries',
        request_serializer=fraft__pb2.Entries.SerializeToString,
        response_deserializer=fraft__pb2.Ack.FromString,
        )


class fRaftServicer(object):
  """fRaft gRPC implementation
  """

  def RequestVote(self, request, context):
    """Takes an ID (use shared IDKey message type) and returns k nodes with
    distance closest to ID requested
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AppendEntries(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_fRaftServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RequestVote': grpc.unary_unary_rpc_method_handler(
          servicer.RequestVote,
          request_deserializer=fraft__pb2.VoteRequest.FromString,
          response_serializer=fraft__pb2.Ack.SerializeToString,
      ),
      'AppendEntries': grpc.unary_unary_rpc_method_handler(
          servicer.AppendEntries,
          request_deserializer=fraft__pb2.Entries.FromString,
          response_serializer=fraft__pb2.Ack.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fRaft', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
