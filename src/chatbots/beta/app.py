import chainlit as cl
import pickle
from keras.models import load_model
import json
from pathlib import Path
# from chatbots.beta.predictions import CommunicateWithChatbot
# import importlib
# importlib.reload(CommunicateWithChatbot)


## TMP
import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import random


class CommunicateWithChatbot:
    def __init__(self, model, words, classes, intents):
        self.model = model
        self.words = words
        self.classes = classes
        self.intents = intents
        self.lemmatizer = WordNetLemmatizer()

    def predict_class(self, sentence):
        """
        Given a sentence/message (e.g. Hello) The method runs prediction using the user query/sentence/message (e.g. Hello)
        And outputs the class with the highest probability

        Args:
            sentence: message (user input)

        Returns:
            Returns a list with the predicted class based on the user input

        Examples :
            [{'intent': 'greeting', 'probability': '0.99833494'}]
        """
        # Predict by passing the sentence to our trained NN model. First we convert the text data into numeric. We use
        # bag-of-words (same method as in the training). When the bag-of-words is created we pass this array to our model
        # and ask for prediction. The model outputs the probabilities of all classes (range is between [0, 1] were 1
        # is the highest. The closer to 1 the more confident the model is for the given class prediction
        p = self.bow(sentence, self.words, show_details=False)
        result = self.model.predict(np.array([p]), verbose=0)[0]

        # filter out predictions below a threshold. We let our model pick a class only if its confidence is above 70%
        error_threshold = 0.7
        results = [[i, r] for i, r in enumerate(result) if r > error_threshold]

        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []

        for r in results:
            return_list.append({"intent": self.classes[r[0]], "probability": str(r[1])})

        return return_list

    def clean_up_sentence(self, sentence):
        # tokenize the pattern - split words into array
        sentence_words = nltk.word_tokenize(sentence)
        # stem each word - create short form for word
        sentence_words = [self.lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words

    def bow(self, sentence, words, show_details=True):
        """
        Return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

        Args:
            sentence:
            words:
            show_details:

        Returns:

        """
        # tokenize the pattern
        sentence_words = self.clean_up_sentence(sentence)
        # bag of words - matrix of N words, vocabulary matrix
        bag = [0] * len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    # assign 1 if current word is in the vocabulary position
                    bag[i] = 1
                    if show_details:
                        print("found in bag: %s" % w)

        return np.array(bag)

    def get_response(self, sentence):
        """
        Provide response to the user a

        Args:
            sentence: User input (message / query)
            intents_json:

        Returns:

        """
        # Get the predicted tags / classes / labels that satisfy the threshold
        tags = self.predict_class(sentence=sentence)

        # Specify a generic response that is returned in case the tags list is empty
        response = "I don't quite understand. Try again or ask a different question."

        if tags:
            tag = tags[0]['intent']  # Get the top one - The class/label with the highest probability

            # Get the object that contains all intents (including the responses)
            list_of_intents = self.intents['intents']

            for item in list_of_intents:
                if item['tag'] == tag:
                    response = random.choice(item['responses'])
                    break

        return response

## TMP

@cl.on_chat_start
def tool(message):
    intents_path = "/Users/syol07091/PycharmProjects/chatbot/src/chatbots/beta/input_data"
    base_path = "/Users/syol07091/PycharmProjects/chatbot/src/chatbots/beta/output_data"
    model = load_model(filepath=str(Path(base_path, 'chatbot_model.h5')))
    words = pickle.load(open(str(Path(base_path, 'words.pkl')), 'rb'))
    classes = pickle.load(open(str(Path(base_path, 'classes.pkl')), 'rb'))
    with open(str(Path(intents_path, 'intents.json'))) as f:
        intents = json.load(f)

    # Predict classes based on a given sentence :
    predictor = CommunicateWithChatbot(model=model, classes=classes, words=words, intents=intents)
    return predictor.get_response(sentence=message)




@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    response = tool(message)

    # Send a response back to the user (Communicate with the Chatbot)
    # await cl.Message(
    #     content=f"Received: {message.content}",
    # ).send()
    await cl.Message(
        content=f"{response}",
    ).send()
