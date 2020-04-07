from typing import Iterator
from uuid import UUID

from dataset_pb2_grpc import DatasetManagerStub, DataManagerStub
from search_pb2_grpc import SearchStub
from dataset_pb2 import Dataset as DatasetPb, Space as SpacePb
from core_pb2 import UUIDRequest, EmptyMessage

from dataset import Dataset

class DatasetManager:

	def __init__(self, conn):
		self._conn = conn
		self._dataset_manager_stub = DatasetManagerStub(conn)
		self._data_manager_stub = DataManagerStub(conn)
		self._search_stub = SearchStub(conn)

	def list(self) -> Iterator[DatasetPb]:
		for pb in self._dataset_manager_stub.List(EmptyMessage()):
			yield pb

	def get(self, id:UUID) -> Dataset:
		proto = self._dataset_manager_stub.Get(UUIDRequest(id=id))

		return Dataset(self._data_manager_stub, self._search_stub, proto)

	def create(self, dim:int, space:SpacePb, partition_count:int=1, replication_factor:int=3) -> Dataset:
		proto = self._dataset_manager_stub.Create(DatasetPb(
			dimension=dim,
			space=space,
			partition_count=partition_count,
			replication_factor=replication_factor
		))

		return Dataset(self._data_manager_stub, self._search_stub, proto)

	def delete(self, id:UUID):
		self._dataset_manager_stub.Delete(UUIDRequest(id=id))