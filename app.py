import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to my application! Enjoy exploring."

@app.route('/how-are-you')
def hello():
    return 'I am good, how about you?'

@app.route('/about')
def about():
    return 'This is a simple Flask application to demonstrate CI/CD.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
