from source.quiz import Quiz
from source.answers import Answers
from source.model import Model_gpt2

q = Quiz()
a = Answers()
while not q.over:
    print(q.get_question())
    answer = input()
    q.process_answer(answer)
    a.process_answer(answer)

m = Model_gpt2(a.answers)
print(m.generate_fortune())
