COHERENCE = {"totally": 0.8, "maybe": 1.0, "as if": 1.5}
PROMPTS = {
    "destined": lambda model_input: destined(model_input),
    "lucky": "",
    "neutral": "",
    "unlucky": "",
    "cursed": "",
}


def destined(model_input):
    return "really blessed prompt with {adventurer_name}, {location}, {objective} embedded.".format(
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
            self.text_prompt = PROMPTS["destined"](self)
            # write my luck state prompts in the above PROMPTS and finish logic to generate prompt here
