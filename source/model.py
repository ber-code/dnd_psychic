import torch as pt
from transformers import GPT2LMHeadModel, GPT2Tokenizer


class Model_gpt2:
    def __init__(self, answers):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.adventurer_name = answers[0]
        self.location = answers[1]
        self.dice_result = int(answers[2])
        self.objective = answers[3]
        self.words_in_fortune = max(150, min(1000, int(answers[4]) * 2))
        if answers[5] == "totally":
            self.coherence = 0.8
        elif answers[5] == "maybe":
            self.coherence = 1.0
        elif answers[5] == "as if":
            self.coherence = 1.5
        if self.dice_result == 20:
            self.sequence = (
                "The luckiest adventurer of all, "
                + self.adventurer_name
                + ", set out towards "
            )
        elif self.dice_result >= 16:
            self.sequence = (
                "The sun was shining and all was well when  "
                + self.adventurer_name
                + " set out towards "
            )
        elif self.dice_result > 10:
            self.sequence = self.adventurer_name + " set out towards "
        elif self.dice_result > 6:
            self.sequence = (
                "It was a cloudy, dreary day when "
                + self.adventurer_name
                + " set out towards "
            )
        elif self.dice_result > 0:
            self.sequence = (
                "Nothing seemed to be going right as "
                + self.adventurer_name
                + " set out towards "
            )
        elif self.dice_reulst == 0:
            self.sequence = (
                self.adventurer_name
                + " felt a chill up their spine as they began their cursed journey towards "
            )
        self.sequence += self.location + " in search of " + self.objective + " ."
        print(self.coherence)

    def generate_fortune(self):
        inputs = self.tokenizer.encode(self.sequence, return_tensors="pt")
        outputs = self.model.generate(
            inputs,
            max_length=self.words_in_fortune,
            do_sample=True,
            temperature=self.coherence,
            top_k=30,
        )
        text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return text
