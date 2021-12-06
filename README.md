# DND Fortune Teller
A client-server modelled networked Dungeons and Dragons styled fortune teller.

The client prompts the user with a series of questions to gather text prompts and functional inputs for the language generation model.

The server receives the responses to the client quiz and generates a custom fortune for the user to add color to their DND session.

## Sample walkthrough
![Sample fortune generation gif](https://github.com/ber-code/dnd_psychic/blob/main/Images/walkthrough_sample.gif)

## Installation
The project relies on [HuggingFace's Transformers](https://huggingface.co/docs/transformers/index) library for interacting with GPT-2 to generate text fortunes.

See requirements.txt for the full list of dependencies.

### 1 - Run the server (in Bash)
1) Open a Bash instance and navigate to the project directory
2) Enter the following commands: "export FLASK_APP=server.py" and "flask run"

### 2 - Run the client (in Bash)
1) Open a separate Bash instance and navigate to the project directory
2) Run 'client.py'
3) Follow text prompts to receive fortune

