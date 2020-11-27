from flask import Flask, render_template

app = Flask(__name__)

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

    
if __name__ == "__main__":
    app.run(debug=True)

