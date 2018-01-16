Required Libraries
- grpc
- string
- random
- concurrent
- time
- sys

Building
- cd ex3
- virtualenv venv OR virtualenv --python=/usr/local/bin/python2.7 venv
- source venv/bin/activate
- python -m pip install --upgrade pip
- python -m pip install grpcio
- python -m pip install grpcio-tools
- pip install concurrent
- chmod +x moderator

# Invoke protoc in order to generate the stubs
- python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. consultation.proto
- python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. debate.proto

# Runing server on localhost
- in another terminal, cd ex3
- python server.py
- ctrl-c to kill server

# Using command line tool
- [ensure server is running on localhost]
- ./moderator <answer OR elaborate> question [blah_run...]

If using 'answer':
- ./moderator answer what is your name

If using 'elaborate':
- ./moderator elaborate taxes 2 4 5# README.txt contains instructions how to build and run your code.
