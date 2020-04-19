# artsonia-autovoter

Python application that automates voting for an artist entry on Artsonia using [selenium](https://pypi.org/project/selenium/).

This project uses [pipenv](https://github.com/pypa/pipenv) to manage the virtual environment and dependencies, and [pylint](https://www.pylint.org/) for code quality.

## Getting Started

### Requirements

* [Python 3.8](https://www.python.org/downloads/) or higher
* [pipenv](https://github.com/pypa/pipenv) 2018.10.9 or higher to support the [.venv file feature](https://github.com/pypa/pipenv/issues/796#issuecomment-429421408)

### Steps

Clone this repo. Then:

Switch to the project directory:  
`> cd artsonia-autovoter`

Install the environment and dependencies:  
`> pipenv install --dev`

Run the program:  
`> pipenv run python vote.py`

## Setup

For posterity, the following are the steps I used to create this project.

Verify pipenv is installed:  
`> pipenv --version`

If not, install it globally:  
`> pip install pipenv`

**OR** install it for the local user only if you wish  (I installed it globally, it works fine):  
`> pip install --user pipenv`

**NOTE:** If you install pipenv for the local user only, add it to PATH for this session. Example for Python 3.8.
Make it permanent by adding it to your PowerShell profile:  
`> $env:Path += ";$env:APPDATA\Python\Python38\Scripts"`

Verify pipenv is in the PATH:  
`> pipenv --version`

Now we're ready to work in the project:  
`> cd artsonia-autovoter`

Initialize the project, which will create a Pipfile and Pipfile.lock, and install [selenium](https://pypi.org/project/selenium/) and [pylint](https://www.pylint.org/) as dev dependencies into the $PROJECT/.virtualenv folder:  
`> pipenv install --dev selenium pylint`

Run it:  
`> pipenv run python vote.py`
