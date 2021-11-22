from source.quiz import Quiz
from source.model_input import ModelInput
from source.model import ModelGPT2
import source.constants as c

q = Quiz()
while not q.over:
    print(q.get_question())
    answer = input()
    q.process_answer(answer)
model_inputs = ModelInput(*q.answers)
model_inputs.generate_prompt()
m = ModelGPT2(model_inputs)
print(m.generate_fortune())
print(c.SATISFIED)
another = input().lower()
if another == c.YES:
    another = 1
else:
    another = False
while another:
    print(m.generate_fortune())
    print(c.ANOTHER)
    another = input().lower()
    if another == c.NO:
        another = False
print(c.GOODBYE.format(payment=q.answers[4]))
