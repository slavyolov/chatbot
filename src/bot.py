# bot.py

from chatterbot import ChatBot
from list_trainer import TrainUsingListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create your chatbot
chatbot = ChatBot(name="Chatspot")

# Specify trainer
trainer = 'corpus'

if trainer == 'list_trainer':
    # Train your chatbot using built in List Trainer
    trainer = TrainUsingListTrainer(chatbot=chatbot)
    trainer.train()
elif trainer == 'corpus':
    # Training using corpus data
    trainer = ChatterBotCorpusTrainer(chatbot=chatbot)
    trainer.train(
        "chatterbot.corpus.english"
    )

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("🙋 ‍> ")
    if query in exit_conditions:
        break
    else:
        print(f"🤖 > {chatbot.get_response(query)}")
