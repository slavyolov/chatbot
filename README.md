# This is a project with education purpose for a 10th grade students (programming schiil in Burgas)

# Pre. requisites :
- Git-flow approach for co-development (releases are nice to have but can be ommitted) 
    - Resources : 
      - https://dev.to/massii/git-flow-vs-github-flow-2iop
      - https://lucamezzalira.com/2014/03/10/git-flow-vs-github-flow/
- Install python version management system (preferably : pyenv)
  - Resources :
    - https://ioflood.com/blog/python-version-manager/
        - installation for MacOS : https://github.com/pyenv/pyenv?tab=readme-ov-file#homebrew-in-macos
        - installation for Windows : https://github.com/pyenv-win/pyenv-win
- IDE (preferably : PyCharm)

# Setup :
1. create a github repository
2. clone locally the project (e.g. https://github.com/slavyolov/chatbot.git)
3. Create a feature branch (feature branch is isolated branch in which every student develops)
   - Please cover the Git-flow approach for co-development

# Steps :
1. Set up the project and the virtual environment. Install the necessary dependencies.
   - Create virtual environment ```python3.8 -m venv ~/venvs/chatbot_alpha```
     - Note : 
   - Activate the virtual environment :
     - Terminal :
       - source ~/venvs/uapc-tpl/bin/activate
     - PyCharm :
       - Open : PyCharm project preferences -> Project -> Python Interpreter → Click on the gearwheel icon → Add... → Virtualenv Environment
       - Add new python interpreter by selecting existing environment :
         - ```/Users/johndoe/venvs/chatbot_alpha/bin/python```
   - Upgrade pip and install wheel package into your virtual environment before installing any other package
     - ```python -m pip install --upgrade pip wheel```
   - With ```pip list``` you can check the installed packages. You should see 3 packages as of now (pip, setuptools, wheel)
   - Install the needed packages / libraries :
     - ```pip install pytz``` 
       - https://pypi.org/project/pytz/
     - ```pip install chatterbot==1.0.4```
       - https://pypi.org/project/ChatterBot/
     - Ideally you should create a requirements.txt file in your project in which you also lock the versions of the libraries that are going to be used in this project. A simple way to do this is by putting them in a requirements.txt file.
       - ```pip freeze > requirements.txt```
       - More on this here : https://dev.to/eskabore/pip-freeze-requirementstxt-a-beginners-guide-5e2m
   - In your project tree. Create 'src' directory. This directory will contain the code for your project
      - Add this as a source directory
   - Add .gitignore file (if not already done)
     - you should have a file named '.gitignore' in the project directory in which you specify the untracked files by git :
       - https://github.com/github/gitignore/blob/main/Python.gitignore
   - Commit and push to the repository the .gitignore and requirements.txt files 
   
2. Create your bot
    - Task : Create a functioning command-line chatbot. Ask him questions and provide feedback.
        - Sub tasks : 
          - Import your chatbot from the installed library ```from chatterbot import ChatBot``` and create an instance of your ChatBot. Specify the name argument of your chatbot (you can be creative here :) )
          - define exit_conditions for your application (e.g. quit)
          - create a while loop that will keep looping unless you enter one of the exit conditions
          - Call the .get_response() method on the ChatBot instance 
          - Play with the bot (ask him questions). What are the answers? Were they good enough?
    - Hints : 
        - When you run bot.py, the ChatterBot may download some NLTK project data and language models. It will print some information about that to your console. Python will not download this data again during subsequent runs.
        - Please use English to communicate with your bot. Currently, it is quite immature to handle conversation in Cyrillic (you may still try it to see what happens)
        - You can add emojis for both players (human and bot) for better user experience 
        - During the first run, our bot (ChatterBot) creates a SQLite database file where it stored all your inputs and connected them with possible responses. There should be three new files that have popped up in your working directory:
          - ├── db.sqlite3 
          - ├── db.sqlite3-shm 
          - └── db.sqlite3-wal
        - For now you can put them into gitignore :
          - ```**/src/db.*```

3. Train your chatbot 

You already know that your chatbot is not very capable to communicate well with humans. What we have to do now is to train him so that it is better prepared for your interesting questions!

- Task : Train your chatbot using ListTrainer (built-in trainers that come with ChatterBot) and english corpus
    - Sub tasks : 
        - upgrade your chatbot with trainer that is using pre-configured questions and answers (list trainer)
        - upgrade your chatbot with trainer that is using pre-configured corpus data
        - make your bot configurable (to use no training, list training and corpus training)
        - What are the limitations you see in the two new approaches (list training and pre-configured corpus data)

- Hints :
  - https://chatterbot.readthedocs.io/en/stable/training.html#training-via-list-data
  - https://chatterbot.readthedocs.io/en/stable/training.html#specifying-corpus-scope
  
4. Extract WhatsApp data (any other chat works too)
   - Specifically, you should save the file to the folder that also contains bot.py and rename it chat.txt.





# Dictionary :
- development process : this is process in which multiple developrs/students collaborate in the same repository. Please familiarize with the Git-flow approach for co-development. 

# Tutorials :
- https://realpython.com/build-a-chatbot-python-chatterbot/#step-1-create-a-chatbot-using-python-chatterbot