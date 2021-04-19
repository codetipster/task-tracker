from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Are you not amazing darling flask?</h1>"