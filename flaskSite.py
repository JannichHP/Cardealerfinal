from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Dyrox.mysql.pythonanywhere-services.com'
app.config['SECRET_KEY'] = "random string"


db = SQLAlchemy(app)

class usersignin(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   Navn = db.Column(db.String(50))
   Efternavn = db.Column(db.String(50))  
   CVR = db.Column(db.String(8))
   Email = db.Column(db.String(100))
   Telefon = db.Column(db.String(8))
   Adgangskode = db.Column(db.String(100))

def __init__(self, Navn, Efternavn, CVR, Email, Telefon, Adgangskode):
   self.Navn = Navn
   self.Efternavn = Efternavn
   self.CVR = CVR
   self.Email = Email
   self.Telefon = Telefon
   self.Adgangskode = Adgangskode

#usersignin.query.filter_by( = ’Toyota’).all()

@app.route("/")
def home():
    return render_template("land_page.html")


@app.route("/signin")
def register_page():
    return render_template("signin.html")


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

