#REFERENCE DBShortCode

# TO USE SEMANTIC-UI AND MODAL


from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, RadioField, BooleanField, validators
from wtforms.validators import DataRequired
from passlib.hash import sha256_crypt
from functools import wraps
from datetime import datetime, date, time

import os
import humanize

app = Flask(__name__)


# SOME DATES AND SIZES TO DEMO
mjhdt = os.path.getmtime('./ref_code/sui-accordion.py')
mjhsz = os.path.getsize('./ref_code/sui-tags.py')


@app.template_filter('size_fmt')
def size_fmt(size):
    return humanize.naturalsize(size)


@app.template_filter('humanize')
def time_humanize(timestamp):
    mdate = datetime.utcfromtimestamp(timestamp)
    return humanize.naturaltime(mdate)


@app.route('/')
def index():
    return render_template('humanize.html', mjhdt=mjhdt, mjhsz=mjhsz)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
