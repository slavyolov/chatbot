# Code is based on :
- https://data-flair.training/blogs/python-chatbot-project/
- https://www.projectpro.io/article/python-chatbot-project-learn-to-build-a-chatbot-from-scratch/429

# Trainig : 
- Task 1 : Run data processing ```data_processing.py```
- Task 2 : Model training ```model_training.py```

# Communication with the Chatbot
- For CLI usage use ```app_cli.py```
- For Chainlit (UI) use ```app.py```
  - Go to '../beta/' directory
  - Run ```chainlit run app.py -w```
      - Results are displayed here : http://localhost:8000
      - cd src/chatbots/beta; chainlit run app.py -d 
      - cd src/chatbots/beta; chainlit run app.py -w

# Език на комуникация
- Ще тренираме бота на английски, но въпросите може да бъдат задавани на български и английски език
- Ще ползваме google translate API за превод на въпросите на английски и после ще връщаме отговор от модела
