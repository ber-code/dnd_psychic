import torch as pt
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# need to rework for new model_inputs being passed in
class ModelGPT2:
    def __init__(self, model_inputs):
        self.model_inputs = model_inputs

    def generate_fortune(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        inputs = self.tokenizer.encode(
            self.model_inputs.text_prompt, return_tensors="pt"
        )
        input_text = self.tokenizer.decode(inputs[0], skip_special_tokens=True)
        outputs = self.model.generate(
            inputs,
            max_length=self.model_inputs.output_wordcap + len(inputs[0]),
            do_sample=True,
            temperature=self.model_inputs.coherence,
            top_k=50,
            no_repeat_ngram_size=2,
        )
        text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return text[len(input_text) :]
