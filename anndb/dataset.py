from typing import List, Iterator, Tuple

from anndb.dataset_pb2_grpc import DataManagerStub
from anndb.search_pb2_grpc import SearchStub
from anndb.dataset_pb2 import Dataset as DatasetPb, InsertRequest, RemoveRequest
from anndb.search_pb2 import SearchRequest

class Dataset:

	def __init__(self, data_manager_stub:DataManagerStub, search_stub:SearchStub, proto:DatasetPb):
		self._data_manager_stub = data_manager_stub
		self._search_stub = search_stub
		self._proto = proto

	@property
	def proto(self):
		return self._proto

	def insert(self, id:int, value:List[float]):
		self._data_manager_stub.Insert(InsertRequest(
			dataset_id=self.proto.id,
			id=id,
			value=value
			))

	def remove(self, id:int):
		self._data_manager_stub.Remove(RemoveRequest(
			dataset_id=self.proto.id,
			id=id,
			))

	def search(self, query:List[float], k:int) -> Iterator[Tuple[int,float]]:
		request = SearchRequest(dataset_id=self.proto.id, query=query, k=k)

		for item in self._search_stub.Search(request):
			yield (item.id, item.score)