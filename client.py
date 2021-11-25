import requests
from source.quiz import Quiz
import source.constants as c
import json

q = Quiz()
while not q.over:
    print(q.get_question())
    answer = input()
    q.process_answer(answer)
model_inputs = json.dumps(q.answers)
response = requests.post("http://127.0.0.1:5000/", model_inputs)
print(response.text)

print(c.SATISFIED)
answer = input().lower()
not_done = answer == c.YES
while not_done:
    response = requests.post("http://127.0.0.1:5000/", model_inputs)
    print(response.text)
    print(c.ANOTHER)
    answer = input().lower()
    if answer == c.NO:
        not_done = False
print(c.GOODBYE.format(payment=q.answers[4]))
