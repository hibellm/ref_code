#REFERENCE DBShortCode

# TO USE SEMANTIC-UI AND MENU/SIDEBAR


from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from data import Vendors
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, RadioField, BooleanField, validators
from wtforms.validators import DataRequired
from passlib.hash import sha256_crypt
from functools import wraps
from datetime import datetime, date, time
import subprocess
import platform
from pymongo import MongoClient  # Database connector
from bson.objectid import ObjectId  # For ObjectId to work
from bson.son import SON
import bson
import datetime as dt
import json


app = Flask(__name__)



client = MongoClient('localhost', 27017)    # Configure the connection to the database
dsidb = client.dsi    # Select the database
dsitrain = dsidb.train


def pingOk(sHost):
    try:
        output = subprocess.check_output(f"ping -{'n' if platform.system().lower()=='windows' else 'c'}  {sHost}", shell=True)
    except Exception as e:
        return False
    return True

# FILTER
@app.template_filter('num2word')
def num2word(num):
    x = {'1': 'one', '2': 'two', '3': 'three', '0': 'four'}
    if num > 4:
        return 'four'
    else:
        return str(x[str(num % 4)])

@app.route('/menu')
def menu():

    # SYSTEM STATUS
    jira = pingOk("127.0.0.1:5003")
    gmail = pingOk("https://127.0.0.1:5000")
    box = pingOk("127.0.0.1:5000")


    # return render_template('menu_sidebar.html')
    return render_template('sui_menu_sidebar.html', jira=jira, gmail=gmail)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/events')
def events():
    return render_template('calendar.html')


@app.route('/delivery')
def delivery():
    return render_template('about.html')


@app.route('/training')
def training():
    # train = dsitrain.find({"visible": 'True'})

    query = {"visible": 'True'}
    train = list(dsitrain.find(query))
    return render_template('training.html', train=train)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
