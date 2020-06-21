from typing import Iterator
from uuid import UUID

from anndb.dataset_pb2_grpc import DatasetManagerStub, DataManagerStub
from anndb.search_pb2_grpc import SearchStub
from anndb.dataset_pb2 import Dataset as DatasetPb, Space as SpacePb, ListDatasetsRequest, GetDatasetRequest
from anndb.core_pb2 import UUIDRequest, EmptyMessage

from anndb.dataset import Dataset

class DatasetManager:

	def __init__(self, conn):
		self._conn = conn
		self._dataset_manager_stub = DatasetManagerStub(conn)
		self._data_manager_stub = DataManagerStub(conn)
		self._search_stub = SearchStub(conn)

	def list(self, with_size:bool=False) -> Iterator[DatasetPb]:
		for pb in self._dataset_manager_stub.List(ListDatasetsRequest(with_size=with_size)):
			yield pb

	def get(self, id:UUID, with_size:bool=False) -> Dataset:
		proto = self._dataset_manager_stub.Get(GetDatasetRequest(dataset_id=id.bytes, with_size=with_size))

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