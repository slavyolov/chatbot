from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam, SGD


def model(train_y: list, train_x: list):
    """
    Create model with 3 layers.

    First layer 128 neurons,
    second layer 64 neurons and
    3rd output layer contains number of neurons equal to number of intents to predict output intent with softmax
    :param train_y:
    :param train_x:
    :return:
    """
    # NN layers
    model = Sequential()
    model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation='softmax'))

    # TODO: task try different optimizers (e.g. Adam, SGD
    # Adam optimization is a stochastic gradient descent method that is based on adaptive estimation of first-order and
        # second-order moments
    # Stochastic Gradient Descent (SGD) is opitimizier with computational efficiency, especially when dealing with large
        # datasets.

    # Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
    # sgd = gradient_descent_v2.SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    adam = Adam(learning_rate=0.01, decay=1e-6)

    model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])

    # fitting and saving the model
    hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
    model.save('chatbot_model.h5', hist)

    print(model.summary())
    print("model created")
