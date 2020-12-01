from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from cardealer.models import User

class RegistrationForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    Company = StringField('Company', validators=[DataRequired(), Length(min=2, max=50)])
    Phone = StringField('Phone', validators=[DataRequired(), Length(min=8, max=8)])
    CVR = StringField('CVR', validators=[DataRequired(), Length(min=7, max=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_Name(self, name):
        user = User.query.filter_by(username=name.data).first()
        if user:
            raise ValidationError('Name is already taken, choose a different')

    def validate_Company(self, company):
        user = User.query.filter_by(company=company.data).first()
        if user:
            raise ValidationError('Company is already registered, choose a different')
    
    def validate_Phone(self, phone):
        user = User.query.filter_by(phone=phone.data).first()
        if user:
            raise ValidationError('Phone number is already taken, choose a different')

    def validate_CVR(self, cvr):
        user = User.query.filter_by(cvr=cvr.data).first()
        if user:
            raise ValidationError('CVR number is already taken, choose a different')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email address is already taken, choose a different')

class LoginForm(FlaskForm):
    CVR = StringField('CVR', validators=[DataRequired(), Length(min=7, max=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
