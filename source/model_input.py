import source.constants as c

COHERENCE = {c.BELIEVE: 0.8, c.UNSURE: 1.0, c.NONBELIEVER: 1.5}


def destined(model_input):
    return c.DESTINED.format(
        adventurer_name=model_input.adventurer_name,
        location=model_input.location,
        objective=model_input.objective,
    )


def lucky(model_input):
    return c.LUCKY.format(
        adventurer_name=model_input.adventurer_name,
        location=model_input.location,
        objective=model_input.objective,
    )


def neutral(model_input):
    return c.NEUTRAL.format(
        adventurer_name=model_input.adventurer_name,
        location=model_input.location,
        objective=model_input.objective,
    )


def unlucky(model_input):
    return c.UNLUCKY.format(
        adventurer_name=model_input.adventurer_name,
        location=model_input.location,
        objective=model_input.objective,
    )


def cursed(model_input):
    return c.CURSED.format(
        adventurer_name=model_input.adventurer_name,
        location=model_input.location,
        objective=model_input.objective,
    )


class ModelInput:
    def __init__(
        self, adventurer_name, location, dice_roll, objective, payment, insight
    ):
        self.adventurer_name = adventurer_name
        self.location = location
        self.dice_roll = dice_roll
        self.objective = objective
        self.coherence = COHERENCE[insight]
        self.output_wordcap = min(max(100, payment * 2), 500)
        self.text_prompt = ""

    def generate_prompt(self):
        if self.dice_roll == 20:
            self.text_prompt = destined(self)
        elif self.dice_roll > 13:
            self.text_prompt = lucky(self)
        elif self.dice_roll > 7:
            self.text_prompt = neutral(self)
        elif self.dice_roll > 1:
            self.text_prompt = unlucky(self)
        elif self.dice_roll == 1:
            self.text_prompt = cursed(self)
