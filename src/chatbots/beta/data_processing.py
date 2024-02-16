from utils.load_files import load_json_file
import nltk
from nltk.stem import WordNetLemmatizer
import pickle


if __name__ == "__main__":
    # Load training data :
    # str(Path(Path(__file__).parents[0]
    file_name = '/Users/syol07091/PycharmProjects/chatbot/src/chatbots/beta/input_data/intents.json'
    intents = load_json_file(filename=file_name)

    # Variables
    words = []
    classes = []
    documents = []
    ignore_words = ['?', '!', '>', '<', '\\', ':', '-', ',', '#','[' , ']', '/', '//', '_', '(', ')']

    # Preprocess data
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            # Step 1 : tokenize each word (word tokenization). Example : 'Hi there' -> ['Hi', 'there']
            # https://neptune.ai/blog/tokenization-in-nlp
            w = nltk.word_tokenize(pattern)
            words.extend(w)

            # Step 2 : combine the words / tokens together (Example : [(['Hi', 'there'], 'greeting')] )
            documents.append((w, intent['tag']))

            # Step 3 : create classes / labels. Example : 'Hi there' is associated to the 'greeting' class
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    # Step 4 : Stemming vs. Lemmatization, lower each word and remove duplicates
    # Preprocess data : Stemming vs. Lemmatization
    # https://databasecamp.de/en/data/stemming-lemmatization
    # Typically, lemmatizers are preferred to stemmer methods because it is a contextual analysis of words rather than
    # using a hard-coded rule to truncate suffixes. This contextuality is especially important when content needs to
    # be specifically understood, as is the case in a chatbot, for example.

    # why lowercasing : the common approach is to reduce everything to lower case for simplicity.
    # why removing duplicated data : Duplicates can significantly impact the quality, accuracy, and reliability of your
        # data, and lead to inaccurate results in your analysis or modeling.
        # Duplicates are an extreme case of nonrandom sampling, and they bias your fitted model.
        # Including them will essentially lead to the model overfitting this subset of points.

    # why ignoring words the 'ignore_words' : because they do not provide a meaningful context for the analysis

    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))

    # sort classes
    classes = sorted(list(set(classes)))

    # Display data
    print(len(classes), "classes", classes)
    print(len(documents), "documents - combination between patterns and intents")
    print(len(words), "unique lemmatized words (our vocabulary)", words)

    # Store pickle files (these are needed for subsequent usage)
    # https://docs.python.org/3/library/pickle.html
    pickle.dump(words, open('/Users/syol07091/PycharmProjects/chatbot/src/chatbots/beta/output_data/words.pkl', 'wb'))
    pickle.dump(classes, open('/Users/syol07091/PycharmProjects/chatbot/src/chatbots/beta/output_data/classes.pkl', 'wb'))
    pickle.dump(documents,
                open('/Users/syol07091/PycharmProjects/chatbot/src/chatbots/beta/output_data/documents.pkl', 'wb'))

    print("Done!")
