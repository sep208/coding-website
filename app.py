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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
