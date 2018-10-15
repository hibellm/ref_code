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

icontypes = {'file audio outline': 'm4a,mp3,oga,ogg,webma,wav', 'file archive outline': '7z,zip,rar,gz,tar', 'file image outline': 'gif,ico,jpe,jpeg,jpg,png,svg,webp', 'file pdf outline': 'pdf', 'file video outline': '3g2,3gp,3gp2,3gpp,mov,qt', 'file code outline': 'atom,plist,bat,bash,c,cmd,coffee,css,hml,js,json,java,less,markdown,md,php,pl,py,rb,rss,sass,scpt,swift,scss,sh,xml,yml', 'file alternate outline': 'txt', 'film': 'mp4,m4v,ogv,webm', 'globe': 'htm,html,mhtm,mhtml,xhtm,xhtml'}

@app.template_filter('icon_fmt')
def icon_fmt(filename):
    i = 'file outline'
    for icon, exts in icontypes.items():
        if filename.split('.')[-1] in exts:
            i = icon
    return i


@app.route('/icons')
def icons():

    a='abc.html'
    b='abc.txt'
    c='abc.zip'
    x='abc.mp3'
    y='abc.txt'
    z='abc.bat'

    a=__name__
    b=__file__
    
    return render_template('icons.html',**locals())

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
