"""

Now, we will create the training data in which we will provide the input and the output.
Our input will be the pattern and output will be the class our input pattern belongs to.
But the computer doesn’t understand text so we will convert text into numbers.

"""

import pickle
import random
from nltk.stem import WordNetLemmatizer
import numpy as np


if __name__ == "__main__":
    # Load needed files :
    classes = pickle.load(open('/Users/syol07091/PycharmProjects/chatbot/src/chatbots/beta/output_data/classes.pkl', 'rb'))
    documents = pickle.load(
        open('/Users/syol07091/PycharmProjects/chatbot/src/chatbots/beta/output_data/documents.pkl', 'rb'))
    words = pickle.load(
        open('/Users/syol07091/PycharmProjects/chatbot/src/chatbots/beta/output_data/words.pkl', 'rb'))

    # create our training data
    training = []

    # create an empty array for our output (classes / labels)
    output_empty = [0] * len(classes)

    # training set, bag of words for each sentence
    for doc in documents:
        # initialize our bag of words
        # Each key is the word, and each value is the number of occurrences of that word in the given text document.
        # BoW1 = {"John":1,"likes":2,"to":1,"watch":1,"movies":2,"Mary":1,"too":1};
        # BoW2 = {"Mary":1,"also":1,"likes":1,"to":1,"watch":1,"football":1,"games":1};
        # https://en.wikipedia.org/wiki/Bag-of-words_model
        bag = []

        # list of tokenized words for the pattern
        pattern_words = doc[0]

        # lemmatize each word - create base word, in attempt to represent related words
        lemmatizer = WordNetLemmatizer()
        pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]

        # Create our bag of words array with 1, if word match found in current pattern
        # A bag-of-words are one-hot encoded (categorical representations of binary vectors) and are extracted
        # features from text to use in modeling. They serve as an excellent vector representation input into our
        # neural network.
        # For our chatbot and use case, the bag-of-words will be used to help the model determine whether the words
        # asked by the user are present in our dataset or not.
        # Note : the bag-of-words equal the words length
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)

        # output is a '0' for each tag and '1' for current tag (for each pattern). The tags are our classes / labels
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        training.append([bag, output_row])

    # shuffle our features and turn into np.array
    # The training variable is list of lists. Every nested list contains : [bag-of-words list, classes list]
    random.shuffle(training)
    training = np.array(training, dtype=object)

    # create train and test lists. X - patterns, Y - intents
    train_x = list(training[:, 0])
    train_y = list(training[:, 1])
    print("Training data created")
