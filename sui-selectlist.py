#!/usr/bin/env python
# -*- coding: utf-8 -*-

# #REFERENCE DBShortCode

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

# GET A LIST FROM SOMEWHERE
mydatalist = ['_ALL_', 'ae_', 'dm_', 'cm_', 'ex_', 'lb_', 'vs_']


@app.route('/selectlist', methods=['GET', 'POST'])
def selectlist():

    if request.method == 'POST':

        toloadlist = request.values.getlist("loadlist")
        print('Load list is :'+str(toloadlist))
        for items in toloadlist:
            print(f'Multiple (max3) select item is :{items}')

        countrylist = request.values.getlist("country")

        country = countrylist[0].split(',')
        print('Country list is :' + str(country))
        for items in country:
            print(f'Country is :{items}')

        # NOW TRY TO RUN THE FUNCTION

        y = dosomething(toloadlist, country)

        return redirect(url_for('selectlist'))
    
    return render_template('selectlist.html', datalist=mydatalist)


def dosomething(data, cntry):

    x = list(zip(data, cntry))
    print(f"The zipped list is: {x}")
    return x




if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
