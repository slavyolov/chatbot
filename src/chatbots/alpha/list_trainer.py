from chatterbot.trainers import ListTrainer


class TrainUsingListTrainer:
    def __init__(self, chatbot):
        self.chatbot = chatbot
        self.trainer = ListTrainer(chatbot=chatbot)

    def train(self):
        self.trainer.train([
                            "Hi there!",
                            "Hello",
                        ])

        self.trainer.train([
            "Are you a plant?",
            "No, I'm the pot below the plant!",
        ])

        self.trainer.train([
            "How are you?",
            "I am good.",
            "That is good to hear.",
            "Thank you",
            "You are welcome.",
        ])
