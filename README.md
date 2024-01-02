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
     
# Dictionary :
- development process : this is process in which multiple developrs/students collaborate in the same repository. Please familiarize with the Git-flow approach for co-development. 
