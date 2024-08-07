#!/usr/bin/env python3
# 0-app.py

""" i18n Exercises(Internationalization) """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Default route"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
