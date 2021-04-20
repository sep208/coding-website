import flask
import random
from flask import  Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

@app.route("/signup.html", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template("signup.html")

if __name__ == '__main__':
   app.run(debug = True)
