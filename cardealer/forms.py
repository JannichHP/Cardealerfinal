from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from cardealer.models import User, CarData

class RegistrationForm(FlaskForm):   #Sets up a registrationForm for the user to create an account where the user must input data in the following fields
    Name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    Company = StringField('Company', validators=[DataRequired(), Length(min=2, max=50)])
    Phone = StringField('Phone', validators=[DataRequired(), Length(min=8, max=8)])
    CVR = StringField('CVR', validators=[DataRequired(), Length(min=7, max=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')   #Clicking the sign up button will start the below process


    #The following validation lines checks the database to see if the given input is already taken by a previously created user
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

    def validate_CVR(self, CVR):
        user = User.query.filter_by(CVR=CVR.data).first()
        if user:
            raise ValidationError('CVR number is already taken, choose a different')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email address is already taken, choose a different')

class LoginForm(FlaskForm):  #Sets up a loginForm for the User, where the user can input data from a previously created account in the following fields
    CVR = StringField('CVR', validators=[DataRequired(), Length(min=7, max=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')  #Ticking the box makes it so the inputet account is remembered the next time the user logs in
    submit = SubmitField('Login')

#Used for updating CVR, Email and Profile picture
class UpdateAccountForm(FlaskForm):
    CVR = StringField('CVR', validators=[Length(min=7, max=8)])    
    email = StringField('Email', validators=[Email()])

    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    #Checks to see if the data the user inputs already is used bby another account in the database

    def validate_CVR(self, CVR):
        if CVR.data != current_user.CVR:
            user = User.query.filter_by(CVR=CVR.data).first()
            if user:
                raise ValidationError('CVR number is already taken, choose a different')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email address is already taken, choose a different')



    #Makes a carForm that asks the user for the below given parameters, afterwards the data from the created car is send to the database
class CarForm(FlaskForm):
    Brand = StringField('Brand', validators=[DataRequired(), Length(min=2, max=50)])
    Model = StringField('Model', validators=[DataRequired(), Length(min=2, max=50)])
    Engine = StringField('Engine', validators=[DataRequired(), Length(min=2, max=50)])
    Colour = StringField('Colour', validators=[DataRequired(), Length(min=2, max=50)])
    Comment = StringField('Comment', validators=[DataRequired(), Length(min=2, max=50)])
    #image_file2 = FileField('Attach picture', validators=[FileAllowed(['jpg', 'png'])])
    
    submit = SubmitField('Post')

   