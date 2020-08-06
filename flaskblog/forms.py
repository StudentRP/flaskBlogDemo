"""
wtforms - pip install flask-wtf

creates forms for html

Better security, validation checks all done resulting in less work
requires email-validator added to interpreter (pip install)

# StringField = field is a string (name seen next to html box, validator)
# Validators = conditions (functions) that must be met in list format
    DataRequired = field must not be empty
    length(min, max)
    EqualTo("field to check against")

"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    """sets username field with min and max char validators"""
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])

    """ check valid email"""
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        """Custom method. Checks database to make sure username not been used before. Notifies in red on entry field."""
        user = User.query.filter_by(username=username.data).first() # checks to see if the user exists
        if user: # if user is None wont throw error
            raise ValidationError('Username taken')

    def validate_email(self, email):
        """Checks database to make sure email not been used before. """
        user = User.query.filter_by(email=email.data).first() # checks to see if the user exists
        if user: # if user is None wont throw error
            raise ValidationError('email already in use')


class LoginForm(FlaskForm):
    """sets username field with min and max char validators"""
    """ check valid email"""

    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField("Login") # login is what you will see on the button
    

"""Require secret key generated to stop modified cookies and cross site forgery attacks"""


"""Goal of form is to get everything to pass as True"""
