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

# Form Class
class Formval(Form):
    name = StringField('name', [validators.Length(min=1)])
    code = StringField('code', [validators.Length(min=1,max=10)])
    desc = TextAreaField('desc', [validators.Length(min=30)])
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])
    agree= BooleanField('I agree.', )
    colour=StringField('Colour [RGB(#, #, #)]')
    colour=StringField('Colour [RGB(#, #, #)]')

@app.route('/formval', methods=['GET','POST'])
def formval():

    #form = Formval(request.form) #THE FORM TO USE

    if request.method == 'POST':# and form.validate():

        #SIMPLE TEXT BOX
        title  = request.values.getlist("title")
        agree  = request.values.getlist("agree")      
        code   = request.values.getlist("code")
        colour = request.values.getlist("colour")

        name1=request.values.getlist("max3sel")
        print('Multiple (max3) select is :'+str(name1))
        for items in name1:
            print('Multiple (max3) select item is :'+(items))
        
        # name2=request.values.get("onesel")
        # print('Single select is :'+str(name2))    
        
        # name3a=request.values.get("tag1")
        # print('Text tag is :'+str(name3a))
        # name3b=request.values.get("tag2")
        # print('Text tag (no default) is :'+str(name3b))

        # name4=request.values.getlist("multsel")
        # print('Multiple select is :'+str(name4))        
        # for items in name4:
        #     print('Multiple select item is :'+(items))

        # name5=request.values.get("fruit")
        # print('Fruit is :'+str(name5))        
        # name6=request.values.get("fruit2") 
        # print('Fruit 2 is :'+str(name6))  #you get 'on' if you dont have a values in teh html part      

        # name7=request.values.get("cbox")
        # print('CheckBox is :'+str(name7))        
        # name8=request.values.get("slider") 
        # print('Slider is :'+str(name8))
        # name9=request.values.get("tog") 
        # print('Toggle is :'+str(name9))

        # name10=request.values.get("slideval") 
        # print('SliderRange is :'+str(name10))

        # name11=request.values.get("throughput") 
        # print('Throughput is :'+str(name11))

    return render_template('formvalidate.html')

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
