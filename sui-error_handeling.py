#REFERENCE DBShortCode

# TO USE SEMANTIC-UI AND MODAL


from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from data import Vendors
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, RadioField, BooleanField, validators
from wtforms.validators import DataRequired
from passlib.hash import sha256_crypt
from functools import wraps
from datetime import datetime, date, time

app = Flask(__name__)

@app.errorhandler(404)
def pageNotFound(error):
    print("page not found")
    msg = 'Custom message for Page Not found (Dismissable - so need javascript as well)'
    return render_template('page_not_found.html', **locals())

@app.errorhandler(500)
def servererror(error):
    msg = 'Custom message for ServerError'
    return render_template('server_error.html',**locals())


if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=False)
