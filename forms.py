from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    Company = StringField('Company', validators=[DataRequired(), Length(min=2, max=50)])
    Phone = StringField('Phone', validators=[DataRequired(), Length(min=8, max=8)])
    CVR = StringField('CVR', validators=[DataRequired(), Length(min=7, max=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    CVR = StringField('CVR', validators=[DataRequired(), Length(min=7, max=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')