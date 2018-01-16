import grpc
import string

import debate_pb2
import debate_pb2_grpc

def run(type, args):

  channel = grpc.insecure_channel('localhost:50051')
  stub = debate_pb2_grpc.CandidateStub(channel)

  if type == "answer":
    # always 2 arguments
    question = string.join(args[0:])
    response = stub.Answer(debate_pb2.AnswerRequest(question=question))

  elif type == "elaborate":
    # 3 or more arguments
    topic = args[0]
    runs = args[1:]
    runs = [int(run) for run in runs]
    response = stub.Elaborate(debate_pb2.ElaborateRequest(topic=topic, blah_run=runs))
  
  print(response.answer)
