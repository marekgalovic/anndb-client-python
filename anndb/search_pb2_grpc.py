# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from anndb import search_pb2 as anndb_dot_search__pb2


class SearchStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Search = channel.unary_stream(
        '/anndb_pb.Search/Search',
        request_serializer=anndb_dot_search__pb2.SearchRequest.SerializeToString,
        response_deserializer=anndb_dot_search__pb2.SearchResultItem.FromString,
        )
    self.SearchPartitions = channel.unary_stream(
        '/anndb_pb.Search/SearchPartitions',
        request_serializer=anndb_dot_search__pb2.SearchPartitionsRequest.SerializeToString,
        response_deserializer=anndb_dot_search__pb2.SearchResultItem.FromString,
        )


class SearchServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Search(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SearchPartitions(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SearchServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Search': grpc.unary_stream_rpc_method_handler(
          servicer.Search,
          request_deserializer=anndb_dot_search__pb2.SearchRequest.FromString,
          response_serializer=anndb_dot_search__pb2.SearchResultItem.SerializeToString,
      ),
      'SearchPartitions': grpc.unary_stream_rpc_method_handler(
          servicer.SearchPartitions,
          request_deserializer=anndb_dot_search__pb2.SearchPartitionsRequest.FromString,
          response_serializer=anndb_dot_search__pb2.SearchResultItem.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'anndb_pb.Search', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
