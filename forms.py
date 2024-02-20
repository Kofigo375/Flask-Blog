from flask_wtf import FlaskForm
## this module will help us use python classes to write html forms 

from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

## creating a sign up form
class RegistrationForm(FlaskForm): 
    ## this class inherits from the main class FlaskForm
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

## creating a log in form
class LoginForm(FlaskForm): 
    ## this class inherits from the main class FlaskForm
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    