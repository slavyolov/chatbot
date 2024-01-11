import chainlit as cl
import pickle
from keras.models import load_model
import json
from pathlib import Path
from predictions import CommunicateWithChatbot


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    def get_response(message):
        """

        Args:
            message:

        Returns:

        """
        intents_path = str(Path(Path(__file__).parents[0], "input_data"))
        base_path = str(Path(Path(__file__).parents[0], "output_data"))
        model = load_model(filepath=str(Path(base_path, 'chatbot_model.h5')))
        words = pickle.load(open(str(Path(base_path, 'words.pkl')), 'rb'))
        classes = pickle.load(open(str(Path(base_path, 'classes.pkl')), 'rb'))
        with open(str(Path(intents_path, 'intents.json'))) as f:
            intents = json.load(f)

        # Predict classes based on a given sentence :
        predictor = CommunicateWithChatbot(model=model, classes=classes, words=words, intents=intents)
        return predictor.get_response(sentence=message)

    # Send a response back to the user (Communicate with the Chatbot)
    await cl.Message(
        content=f"{get_response(message.content)}",
    ).send()
