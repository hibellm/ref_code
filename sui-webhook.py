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
from datetime import datetime, date, time, timezone
import requests
import pickle
from executecmd import runcode
import humanize


app = Flask(__name__)


@app.template_filter('humanize')
def time_humanize(timestamp):
    mdate = datetime.utcfromtimestamp(timestamp)
    return humanize.naturaltime(mdate)


@app.route('/')
def route():
    return "welcome Marcus"

@app.route('/github', methods=['GET', 'POST'])
def github():

    # THE WEBHOOK CONTENT INTO A PICKLE FOR LATER USE
    _jsonres = request.json


    if request.headers['X-Github-Event'] == 'ping':
        print(f"This was a {request.headers['X-Github-Event']} event!")
        #LOAD THE EXISTING JSON THEN ADD THE NEW
        allpings = pickle.load(open("save.allpings", "rb"))
        allpings = (allpings, _jsonres)
        pickle.dump(allpings, open("save.allpings", "wb"))

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
    y = pickle.load(open("save.allpings", "rb"))
    # print(f'y is: {y}')

    ping = datetime.now().timestamp() + 2 * 60 * 60
    #GET SOME VALUES FROM THE PAYLOAD
    # ping=y['hook']['updated_at']
    # pingdt = datetime.strptime(ping, "%Y-%m-%dT%H:%M:%SZ")


    x, z = runcode('python sample-python.py', '.')



    # return fromgithub
    return render_template('webhook.html', x=x, y=y, ping=ping)




if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)

#To run , expose the flask port to github..using ngrok (ngrok http <port>)
# https://www.youtube.com/watch?v=YMBzb_RBDAA