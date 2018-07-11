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


@app.route('/form', methods=['GET','POST'])
def form():

    if request.method == 'POST':

        name1=request.values.getlist("max3sel")
        print('Multiple (max3) select is :'+str(name1))
        for items in name1:
            print('Multiple (max3) select item is :'+(items))
        
        name2=request.values.get("onesel")
        print('Single select is :'+str(name2))    
        
        name3a=request.values.get("tag1")
        print('Text tag is :'+str(name3a))
        name3b=request.values.get("tag2")
        print('Text tag (no default) is :'+str(name3b))

        name4=request.values.getlist("multsel")
        print('Multiple select is :'+str(name4))        
        for items in name4:
            print('Multiple select item is :'+(items))
        

    return render_template('form.html')

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
