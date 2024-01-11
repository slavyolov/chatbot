# bot.py

from chatterbot import ChatBot
from list_trainer import TrainUsingListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from text_cleaner import TextCleaner
from pathlib import Path

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
elif trainer == 'custom_corpus':
    # Training using custom corpus made from chats
    CORPUS_FILE = str(Path(Path(__file__).parents[0], "input_data/chat.txt"))
    cleaned_corpus = TextCleaner(chat_file=CORPUS_FILE).clean_corpus()
    trainer = ListTrainer(chatbot)
    trainer.train(conversation=cleaned_corpus)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("🙋 ‍> ")
    if query in exit_conditions:
        break
    else:
        print(f"🤖 > {chatbot.get_response(query)}")
