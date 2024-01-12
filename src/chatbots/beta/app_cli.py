import pickle
from keras.models import load_model
from utils.load_files import load_json_file
from pathlib import Path
from chatbots.beta.predictions import CommunicateWithChatbot


if __name__ == "__main__":
    intents_path = str(Path(Path(__file__).parents[0], "input_data"))
    base_path = str(Path(Path(__file__).parents[0], "output_data"))
    model = load_model(filepath=str(Path(base_path, 'chatbot_model.h5')))
    intents = load_json_file(filename=str(Path(intents_path, 'intents.json')))
    words = pickle.load(open(str(Path(base_path, 'words.pkl')), 'rb'))
    classes = pickle.load(open(str(Path(base_path, 'classes.pkl')), 'rb'))

    # Predict classes based on a given sentence :
    predictor = CommunicateWithChatbot(model=model, classes=classes, words=words, intents=intents)

    # Communicate with the Chatbot in the Console CLI
    exit_conditions = (":q", "quit", "exit")
    while True:
        message = input("🙋 ‍> ")
        if message in exit_conditions:
            break
        print(f"🤖 > {predictor.get_response(sentence=message)}")
