from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label="Enter a Username")
    email_address = StringField(label="Email")
    password1 = PasswordField(label="Enter password")
    password2 = PasswordField(label="Confirm password")
    submit = SubmitField(label="Submit")



