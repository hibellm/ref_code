#!/usr/bin/env python
# -*- coding: utf-8 -*-

# #REFERENCE DBShortCode

# TO USE SEMANTIC-UI AND MODAL

from flask import Flask, render_template, json, flash, redirect, url_for, session, request, logging
# from data import Vendors
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, RadioField, BooleanField, validators
from wtforms.validators import DataRequired
from passlib.hash import sha256_crypt
from functools import wraps
from datetime import datetime, date, time
import requests
import pickle

app = Flask(__name__)

@app.route('/')
def route():
    return "welcome Marcus"



@app.route('/github', methods=['GET', 'POST'])
def github():

    # THE WEBHOOK CONTENT INTO A PICKLE FOR LATER USE
    _jsonres = request.json
    pickle.dump(_jsonres, open("save.gh", "wb"))

    if request.headers['X-Github-Event'] == 'ping':
        print(f"This was a {request.headers['X-Github-Event']} event!")
    elif request.headers['X-Github-Event'] == 'push':
        print(f"This was a {request.headers['X-Github-Event']} event!")
    elif request.headers['X-Github-Event'] == 'action':
        print(f"This was a {request.headers['X-Github-Event']} event!")
    else:
        print(f"This was a {request.headers['X-Github-Event']} event!")

    # THE WEBHOOK PAYLOAD AS A STRING TO RETURN!
    _jsonress = json.dumps(_jsonres)
    # print(_jsonress)

    return _jsonress



@app.route('/whgithub', methods=['GET', 'POST'])
def whgithub():
    # LOAD THE WEBHOOK PAYLOAD AND DISPLAY
    y = pickle.load(open("save.gh", "rb"))
    print(f'y is: {y}')

    # return fromgithub
    return render_template('webhook.html', y=y)




if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)

#To run , expose the flask port to github..using ngrok (ngrok http <port>)
# https://www.youtube.com/watch?v=YMBzb_RBDAA