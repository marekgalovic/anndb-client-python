compile_protos:
	python -m grpc_tools.protoc -I ./proto --python_out=. --grpc_python_out=. ./proto/anndb/*.proto