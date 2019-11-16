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

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)


icontypes = {'file audio': 'm4a,mp3,oga,ogg,webma,wav',
             'file archive': '7z,zip,rar,gz,tar',
             'file picture': 'gif,ico,jpe,jpeg,jpg,png,svg,webp',
             'file pdf': 'pdf',
             'file word': 'doc,docx',
             'file excel': 'xls,xlsx',
             'file film': '3g2,3gp,3gp2,3gpp,mov,qt',
             'file code': 'atom,plist,bat,bash,c,cmd,coffee,css,hml,js,json,java,less,markdown,md,php,pl,py,rb,rss,sass,scpt,swift,scss,sh,xml,yml',
             'file text': 'txt',
             'file video': 'mp4,m4v,ogv,webm',
             'globe': 'htm,html,mhtm,mhtml,xhtm,xhtml'}


@app.route('/formdragdrop', methods=['GET', 'POST'])
def formdragdrop():

    try:
        cur = mysql.connection.cursor()
        print('Connection worked!')
        # Get roles
        result = cur.execute("SELECT * FROM rwd_meta_mdh.event_log")
        events = cur.fetchall()

        # Get roles
        result = cur.execute("SELECT * FROM sys.schema_table_statistics where table_schema like 'study%' ")
        tables = cur.fetchall()

        # # Get Roles for Dropdown
        result = cur.execute("SELECT * FROM rwd_meta_mdh.event_log group by eventtype")
        eventsd = cur.fetchall()

    except Exception as e:
        pass

    if request.method == 'POST':

        name1 = request.values.get("div1")
        # name1 = request.values("div1")
        # text = request.form['mjh']
        print(f"mjh0 {request.form['mjh0']}")
        print(f"mjh1 {request.form['mjh1']}")
        print(f"mjh2 {request.form['mjh2']}")
        print(f"mjh3 {request.form['mjh3']}")
        print(f"mjh4 {request.form['mjh4']}")
        print(f"mjh5 {request.form['mjh5']}")
        print(f"sel1 {request.form['sel1']}")

        return redirect(url_for('formdragdrop'))
    
    return render_template('formdragdrop.html', result=result, eventsd=eventsd, tables=tables)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True, port=5000)

