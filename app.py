from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, version 1 changes for New Feature"