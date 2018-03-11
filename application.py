#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import User

app = Flask(__name__, static_folder = "./frontend/dist/static",
            template_folder = "./frontend/dist")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
