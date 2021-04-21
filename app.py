import random
from flask import Flask, redirect, url_for, render_template, request

from db import get_db
from users_db import create_users_table
from auth import signup_user

app = Flask(__name__)

with app.app_context():
    create_users_table()


@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='POST':
        # not sure what POST will be on home route
        pass
    return render_template('index.html')


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        signup_user(username, email, password)   
        return redirect(url_for("home")) 

    return render_template("signup.html")


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)