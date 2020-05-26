#REFERENCE DBShortCode

# TO USE SEMANTIC-UI AND CARD LAYOUTS

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from data import Vendors
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, RadioField, BooleanField, validators
from wtforms.validators import DataRequired
from passlib.hash import sha256_crypt
from functools import wraps
from datetime import datetime, date, time

app = Flask(__name__)

@app.route('/cards')
def cards():

    return render_template('cards.html', **locals())


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
