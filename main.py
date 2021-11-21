from source.quiz import Quiz
from source.model_input import ModelInput
from source.model import ModelGPT2

q = Quiz()
while not q.over:
    print(q.get_question())
    answer = input()
    q.process_answer(answer)
model_inputs = ModelInput(*q.answers)
model_inputs.generate_prompt()
m = ModelGPT2(model_inputs)
print(m.generate_fortune())
