# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import cluster_pb2 as cluster__pb2
import core_pb2 as core__pb2


class NodesManagerStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListNodes = channel.unary_stream(
                '/anndb_pb.NodesManager/ListNodes',
                request_serializer=core__pb2.EmptyMessage.SerializeToString,
                response_deserializer=cluster__pb2.Node.FromString,
                )
        self.AddNode = channel.unary_stream(
                '/anndb_pb.NodesManager/AddNode',
                request_serializer=cluster__pb2.Node.SerializeToString,
                response_deserializer=cluster__pb2.Node.FromString,
                )
        self.RemoveNode = channel.unary_unary(
                '/anndb_pb.NodesManager/RemoveNode',
                request_serializer=cluster__pb2.Node.SerializeToString,
                response_deserializer=core__pb2.EmptyMessage.FromString,
                )


class NodesManagerServicer(object):
    """Missing associated documentation comment in .proto file"""

    def ListNodes(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddNode(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveNode(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NodesManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListNodes': grpc.unary_stream_rpc_method_handler(
                    servicer.ListNodes,
                    request_deserializer=core__pb2.EmptyMessage.FromString,
                    response_serializer=cluster__pb2.Node.SerializeToString,
            ),
            'AddNode': grpc.unary_stream_rpc_method_handler(
                    servicer.AddNode,
                    request_deserializer=cluster__pb2.Node.FromString,
                    response_serializer=cluster__pb2.Node.SerializeToString,
            ),
            'RemoveNode': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveNode,
                    request_deserializer=cluster__pb2.Node.FromString,
                    response_serializer=core__pb2.EmptyMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'anndb_pb.NodesManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NodesManager(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def ListNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/anndb_pb.NodesManager/ListNodes',
            core__pb2.EmptyMessage.SerializeToString,
            cluster__pb2.Node.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/anndb_pb.NodesManager/AddNode',
            cluster__pb2.Node.SerializeToString,
            cluster__pb2.Node.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/anndb_pb.NodesManager/RemoveNode',
            cluster__pb2.Node.SerializeToString,
            core__pb2.EmptyMessage.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)