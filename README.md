#  SET UP

 Ensure the following requirements are up and running;
 - Python 3.8
 - Visual studio code as an IDE
 - Flask
 
 ## Setting up the project
 First, lets try to serve a simple flask page.
 run `$pip install flask`
if this doesn't run, please check your python version or run `pip3` instead of `pip`

check if flask is installed:
`$flask --version`
this should out put your default python version and a wsgi version along side you flask version. As of the time of writting this, flask 1.1.2 was the stable flask version

create a simple python file within(`market.py`) the root project directory, in our case../home/usr/Desktop/Flask-project/task-tracker/market.py

paste this in the file you just created:

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

run:
  `export FLASK_APP=market.py`

then run:
  `flask run`
to serve the basic "Hello World".

Congratulations, you just served a basic script using flask.
