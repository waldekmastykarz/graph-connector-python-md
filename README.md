# 

## Prerequisites

- [Microsoft Graph CLI](https://devblogs.microsoft.com/microsoft365dev/microsoft-graph-cli-v1-0-0-release-candidate-now-with-beta-support/)
- [jq](https://jqlang.github.io/jq/)

## Minimal Path to Awesome

```sh
# make the setup script executable
chmod +x ./setup.sh
# create Entra app
./setup.sh
# ensure you've got Python 3.11 installed
pyenv install 3.11
# use Python 3.11 in the project
pyenv local 3.11
# create virtual environment
python3 -m venv venv
# activate virtual environment
source venv/bin/activate
# restore dependencies
pip install -r requirements.txt
# create connection
python3 main.py create-connection
# load content
python3 main.py load-content
# deactivate virtual environment
deactivate
```
