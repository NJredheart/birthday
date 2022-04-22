from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

@app.route("/")
def home():
        return render_template("index.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/sorry")
def sorry():
    return render_template("sorry.html")
@app.route("/bdy")
def bdy():
    return render_template("bdy.html")

if __name__ == "__main__":
     app.run(debug=True)