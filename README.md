# What?
This is an RPC service that simulates a debate using RPCs. There's a simple command line tool that wraps an RPC client that makes calls to the service.

Also, the RPC service will make calls to an external RPC service that will help it construct evasive answers to debate questions. The external service is configured to run on the IP address `23.236.49.28` on port `50051`.

Clearer instructions here: https://docs.google.com/document/d/1r-T7DBCCh9dxpMCO05azCOXkj90Z9__wz87awK2Fsh4/edit?usp=sharing

## Building
```
virtualenv venv OR virtualenv --python=/usr/local/bin/python2.7 venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install grpcio
python -m pip install grpcio-tools
pip install concurrent
chmod +x moderator
```

## Invoke protoc in order to generate the stubs
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. consultation.proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. debate.proto
```

## Runing server in another terminal
```
python server.py
```

# Usage
After ensuring server is running
```
./moderator <answer OR elaborate> question [blah_run...]
```
---

## If using `answer`:
```
./moderator answer what is your name
```
Possible reply would be: **You asked me: what is my name but I want to say that: I promise a Tinder account to every citizen**

---

## If using `elaborate`:
```
./moderator elaborate taxes 2 4 5
```
Reply would be: **blah blah taxes blah blah blah blah taxes blah blah blah blah blah**

