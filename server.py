from flask import Flask, request
from source.model import ModelGPT2
from source.model_input import ModelInput
import json

app = Flask(__name__)
fortune = ""


@app.route("/", methods=["POST"])
def generate_fortune():
    global fortune
    model_inputs = ModelInput(*json.loads(request.data))
    model_inputs.generate_prompt()
    m = ModelGPT2(model_inputs)
    fortune = m.generate_fortune()
    return fortune + "..."


@app.route("/fortune")
def last_fortune():
    return fortune + "..."
