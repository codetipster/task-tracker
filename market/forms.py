from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('username already exists!')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email already in use, pls try another email!')        

    username = StringField(label="Enter a Username",validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label="Email Address", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Enter password", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirm password", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Create Account")

class LoginForm(FlaskForm):

    username = StringField(label="Enter username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Sign In")

