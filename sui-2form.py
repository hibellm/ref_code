#REFERENCE https://stackoverflow.com/questions/18290142/multiple-forms-in-a-single-page-using-flask-and-wtforms

# TO USE SEMANTIC-UI AND MODAL

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, RadioField, BooleanField, validators
from wtforms.validators import DataRequired
from passlib.hash import sha256_crypt
from functools import wraps
from datetime import datetime, date, time

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MYSQL
mysql = MySQL(app)

class RegisterForm(Form):
    name = StringField('name')
    submit1 = SubmitField('submit')

class LoginForm(Form):
    name = StringField('name')
    submit2 = SubmitField('submit')

@app.route('/')
def index():
    register_form = RegisterForm()
    login_form = LoginForm()
    return render_template('2form.html', register_form=register_form, login_form=login_form)

@app.route('/register', methods=['POST'])
def register():
    register_form = RegisterForm()
    login_form = LoginForm()

    if register_form.validate_on_submit():
        ...  # handle the register form
    # render the same template to pass the error message
    # or pass `form.errors` with `flash()` or `session` then redirect to /
    return render_template('2from.html', register_form=register_form, login_form=login_form)


@app.route('/login', methods=['POST'])
def login():
    register_form = RegisterForm()
    login_form = LoginForm()

    if login_form.validate_on_submit():
        ...  # handle the login form
    # render the same template to pass the error message
    # or pass `form.errors` with `flash()` or `session` then redirect to /
    return render_template('2from.html', register_form=register_form, login_form=login_form)

        
if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
