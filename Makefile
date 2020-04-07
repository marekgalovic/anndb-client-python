compile_protos:
	python -m grpc_tools.protoc -I ./proto --python_out=./anndb --grpc_python_out=./anndb ./proto/*.proto