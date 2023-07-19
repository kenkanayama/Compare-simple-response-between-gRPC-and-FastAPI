#!/bin/bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./helloworld.proto && watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- python server.py