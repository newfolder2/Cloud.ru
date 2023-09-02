from flask import Flask
import os
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/hi')
def hi():
    return "HI YOURSELF!"

@app.route('/hostname')
def hostname():
    return os.uname()[1]

@app.route('/author')
def author():
    #os.environ["AUTHOR"] = "Alena"
    return os.environ["AUTHOR"]

@app.route('/id')
def id():
    #os.environ["UUID"] = str(uuid.uuid4())
    return os.environ["UUID"]
