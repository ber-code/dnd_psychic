def intro_name(quiz):
    return "'So you’ve come for the benefit of the Blind Seer’s vision… What is your name, adventurer?'"


def location(quiz):
    return "'Oh {adventurer_name} there are so many paths before you, and I can see them all! But you have free will, so pray tell me, where do you plan to go today?'".format(
        adventurer_name=quiz.answers[0]
    )


def dice_roll(quiz):
    return "'I can just see it now… surely you must be eager… roll your icosa-sided dice and tell me the result.'"


def objective(quiz):
    return "'I can sense there is something you seek. Describe it for the scryer, if you so desire.'"


def payment(quiz):
    return "'It is clear as day… I can feel the spirits guiding my tongue. There is just the matter of the sacrificial coins. What? No of course I don’t keep them – the spirits take them away! How much copper is a clear vision of the future worth to you, hmm?'"


def insight(quiz):
    return "The Seer's cloudy eyes roll back. As they commune with the spirits you ask yourself: 'Do I really believe this mumbo-jumbo?' ('Totally', 'Maybe', 'As if')"


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
            if not answer.isdigit() or int(answer) > 20 or int(answer) < 11:
                print(
                    "'Don't they teach Greek in your universe? 'Icosa' means 20. Am I old?'"
                )
                answer = input()
            while not answer.isdigit() or int(answer) > 20 or int(answer) < 1:
                print("'I told you what 'icosa' means. Roll a real D20!'")
                answer = input()
            answer = int(answer)
            if answer == 20:
                print("'Bless the skies - nat' 20 before my very eyes!'")
            elif answer == 1:
                print(
                    "The blind lady fixes her eyes on you and blinks repeatedly. 'The last person who rolled a... oh, nevermind!'."
                )
        if self.q_ptr == 3:
            pass
        if self.q_ptr == 4:
            while not answer.isdigit():
                print(
                    "'I'm blind but I know what bronze pieces feel like. How much is this vision worth to you?'"
                )
                answer = input()
            answer = int(answer)
            if answer > 100:
                print("You're in for a real yarn my friend!")
        if self.q_ptr == len(QUESTIONS) - 1:
            answer = answer.lower()
            while answer not in set(["totally", "maybe", "as if"]):
                print("Be honest. 'Totally' , 'Maybe', or 'As if'.")
                answer = input().lower()
        self.answers[self.q_ptr] = answer
        self.q_ptr += 1
        if self.q_ptr >= len(QUESTIONS):
            self.over = True
