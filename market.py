from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Are you not amazing darling flask?</h1>"

# LESSONS ON DYNAMIC RENDERING: Think of how FB will have to hard code route functions for individual profiles 
# @app.route('/About/<username>')
# def about_us(username):
#     return f'<h1>We are great devs for the future, this is {username}</h1>'    