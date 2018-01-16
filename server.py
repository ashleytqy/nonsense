from concurrent import futures
import time
import grpc
import string
import random

import debate_pb2
import debate_pb2_grpc

import consultation_pb2
import consultation_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class Candidate(debate_pb2_grpc.CandidateServicer):

  def Answer(self, request, context):
    question = request.question
    first_word = question.split(' ', 1)[0]

    words = ['why', 'what', 'how', 'who', 'when']

    if not any(first_word.lower() in w for w in words):
      rand = random.randint(0, 1)

      if rand == 1:
        response = 'your 3 cent titanium tax goes too far'
      else:
        response ='your 3 cent titanium tax doesn\'t go too far enough'

    else:
      # replaces all occurrences of the word 'You' with 'I'
      # and all occurrences of the word 'your' with 'my'
      post_replacement = ' '.join('I' if word.lower() == 'you' else word for word in question.split())
      post_replacement = ' '.join('my' if word.lower() == 'your' else word for word in post_replacement.split())

      # Makes an RPC call with question to the external CampaignManager.Retort service
      channel = grpc.insecure_channel('23.236.49.28:50051')
      stub = consultation_pb2_grpc.CampaignManagerStub(channel)
      retort = stub.Retort(consultation_pb2.RetortRequest(original_question=question)).retort

      response = 'You asked me: ' + post_replacement + ' but I want to say that: ' + retort
    return debate_pb2.AnswerReply(answer=response)

  def Elaborate(self, request, context):
    # response has repeated runs of the word 'blah' separated by 'topic'
    # the length of each 'blah' run corresponds to a value of 'blah_run', in the order it appears
    # if there is a single run, 'topic' is printed after it
    # when there are no runs, only 'topic' is printed

    runs = request.blah_run
    topic = request.topic

    response = ''
    if len(runs) == 0:
      response = topic
    elif len(runs) == 1:
      response = 'blah ' + topic
    else:
      for (index, run) in enumerate(runs):
        response += ('blah ' * run)
        if index < len(runs) - 1:
          response += topic + ' '

    return debate_pb2.ElaborateReply(answer=response)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  debate_pb2_grpc.add_CandidateServicer_to_server(Candidate(), server)
  server.add_insecure_port('localhost:50051')
  server.start()
  print("hi from server!")
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
