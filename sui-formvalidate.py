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


@app.route('/formval', methods=['GET','POST'])
def formval():

    if request.method == 'POST':

        #SIMPLE TEXT BOX
        name1=request.values.getlist("max3sel")
        print('Multiple (max3) select is :'+str(name1))
        for items in name1:
            print('Multiple (max3) select item is :'+(items))
        
  
        m2agree=request.values.get("agree")
        print('Checkbox agree is :'+str(m2agree))          
        if request.form.get('agree'):
            print('So you have agreed!')   

    return render_template('formvalidate.html')

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
