import os
from flask import Flask
from flask import render_template

from app import create_app

app = create_app('dev')

@app.route("/")
def home():
    return "Starts flask app"


if __name__ == '__main__':
    app.run()
