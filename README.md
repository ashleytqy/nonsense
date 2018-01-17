# Building
```
virtualenv venv OR virtualenv --python=/usr/local/bin/python2.7 venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install grpcio
python -m pip install grpcio-tools
pip install concurrent
chmod +x moderator
```

# Invoke protoc in order to generate the stubs
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. consultation.proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. debate.proto
```

# Runing server on localhost
In another terminal
```
python server.py
```

# Using command line tool
Ensure server is running on localhost
```
./moderator <answer OR elaborate> question [blah_run...]
```

If using 'answer':
```
./moderator answer what is your name
```

If using 'elaborate':
```
./moderator elaborate taxes 2 4 5
```

