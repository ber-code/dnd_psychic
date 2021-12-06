import source.constants as c
from source.utils import slow_print


def intro_name(quiz):
    return c.INTRO


def location(quiz):
    return c.LOCATION.format(adventurer_name=quiz.answers[0])


def dice_roll(quiz):
    return c.REQUEST_ROLL


def objective(quiz):
    return c.OBJECTIVE


def payment(quiz):
    return c.PAYMENT


def insight(quiz):
    return c.INSIGHT


QUESTIONS = [
    lambda quiz: intro_name(quiz),
    lambda quiz: location(quiz),
    lambda quiz: dice_roll(quiz),
    lambda quiz: objective(quiz),
    lambda quiz: payment(quiz),
    lambda quiz: insight(quiz),
]


class Quiz:
    def __init__(self):
        self.q_ptr = 0
        self.answers = [None] * len(QUESTIONS)
        self.over = False

    def get_question(self):
        return QUESTIONS[self.q_ptr](self)

    def process_answer(self, answer):
        if self.q_ptr == 0:
            pass
        if self.q_ptr == 1:
            pass
        if self.q_ptr == 2:
            if not answer.isdigit() or int(answer) > 20 or int(answer) < 1:
                slow_print(c.INVAL_DICE_ONE)
                answer = input()
            while not answer.isdigit() or int(answer) > 20 or int(answer) < 1:
                slow_print(c.INVAL_DICE_TWO)
                answer = input()
            answer = int(answer)
            if answer == 20:
                slow_print(c.NAT_TWENTY)
            elif answer == 1:
                slow_print(c.NAT_ONE)
        if self.q_ptr == 3:
            pass
        if self.q_ptr == 4:
            while not answer.isdigit():
                slow_print(c.INVAL_PAYMENT)
                answer = input()
            answer = int(answer)
            if answer > 100:
                slow_print(c.GENEROUS)
        if self.q_ptr == len(QUESTIONS) - 1:
            answer = answer.lower()
            while answer not in set([c.BELIEVE, c.UNSURE, c.NONBELIEVER]):
                slow_print(c.INVAL_INSIGHT)
                answer = input().lower()
        self.answers[self.q_ptr] = answer
        self.q_ptr += 1
        if self.q_ptr >= len(QUESTIONS):
            self.over = True
