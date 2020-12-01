from flask import render_template, url_for, flash, redirect
from cardealer import app, db, bcrypt
from cardealer.forms import RegistrationForm, LoginForm
from cardealer.models import User, Post
from flask_login import login_user


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.Name.data, company=form.Company.data, phone=form.Phone.data, cvr=form.CVR.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login_page'))
    return render_template("register.html", title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(cvr=form.CVR.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Login Successful!', 'success')
            return redirect(url_for('land_page'))
        else:
            flash('Login Unsuccessful. Please Check username and password', 'danger')
    return render_template("login.html", title='Login', form=form)


@app.route("/land_page")
def land_page():
    return render_template("land_page.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")