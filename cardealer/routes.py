from flask import render_template, url_for, flash, redirect
from cardealer import app, db, bcrypt
from cardealer.forms import RegistrationForm, LoginForm
from cardealer.models import User, Post


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