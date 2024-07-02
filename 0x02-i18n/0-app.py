#!/usr/bin/env python3
# 0-app.py

""" i18n Exercises(Internationalization) """
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Home route"""
    return render_template('0-index.html')
