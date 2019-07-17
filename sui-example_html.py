#!/usr/bin/env python
# -*- coding: utf-8 -*-

# #REFERENCE DBShortCode

# TO USE SEMANTIC-UI AND MODAL

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_cors import CORS, cross_origin
from functools import update_wrapper

#from data import Vendors
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, RadioField, BooleanField, validators
from wtforms.validators import DataRequired
from passlib.hash import sha256_crypt
from functools import wraps
from datetime import datetime, date, time

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})


# app.config['Access-Control-Allow-Headers'] = ('Cache-Control, Pragma, Origin, Authorization,' 'Content-Type, X-Requested-With')


# GET A LIST FROM SOMEWHERE
mydatalist = ['_ALL_', 'ae_', 'dm_', 'cm_', 'ex_', 'lb_', 'vs_']


@app.route('/example_elements')
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization','access-control-allow-origin'])
def selectlist():
    return render_template('example_elements.html', datalist=mydatalist)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
