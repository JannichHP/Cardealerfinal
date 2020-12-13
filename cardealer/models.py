from flask import current_app
from cardealer import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin): #Creates a class named User
    id = db.Column(db.Integer, primary_key=True)  #Sets id to be a unique ID set an an int
    username = db.Column(db.String(20), unique=True, nullable=False)  #Sets it to be a max string of 20 chars, makes it unique
    company = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(100), unique=True, nullable=False)   #Nullable makes it so the field must contain data
    CVR = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='avatar.png')   #Sets it so the profile is always created with a defualt picture "avatar"
    cardatas = db.relationship('CarData', backref='user', lazy=False)  #Creates a relationship with the class "CarData"
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class CarData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Brand = db.Column(db.String(100), nullable=False)
    Model = db.Column(db.String(500), nullable=False)
    Engine = db.Column(db.String(100), nullable=False)
    Colour = db.Column(db.String(100), nullable=False)
    Comment = db.Column(db.String(100), nullable=False)
    #image_file2 = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   #Connects this class to the "User" class


    def __repr__(self):
        return f"Cardata('{self.Brand}', '{self.Model}')"