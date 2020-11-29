from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '2b3b0653a9d3c42948bd5edce8fd84cb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User, Post

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.Name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        if form.CVR.data == '20202020' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Login Unsuccessful. Please Check username and password', 'danger')
    return render_template("login.html", title='Login', form=form)


@app.route("/land_page")
def land_page():
    return render_template("land_page.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)

