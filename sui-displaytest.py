#REFERENCE DBShortCode

# TO USE SEMANTIC-UI AND CONNECTION TO DATABASES

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
app.config['MYSQL_DB'] = 'dsi'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

icontypes = {'file audio': 'm4a,mp3,oga,ogg,webma,wav', 'file archive': '7z,zip,rar,gz,tar', 'file picture': 'gif,ico,jpe,jpeg,jpg,png,svg,webp', 'file pdf': 'pdf', 'file word': 'doc,docx', 'file excel': 'xls,xlsx', 'file film': '3g2,3gp,3gp2,3gpp,mov,qt', 'file code': 'atom,plist,bat,bash,c,cmd,coffee,css,hml,js,json,java,less,markdown,md,php,pl,py,rb,rss,sass,scpt,swift,scss,sh,xml,yml', 'file text': 'txt', 'file video': 'mp4,m4v,ogv,webm', 'globe': 'htm,html,mhtm,mhtml,xhtm,xhtml'}


@app.route('/display')
def jinjacontrol():
    
    #TEST CONNECTION
    try:
        cur = mysql.connection.cursor()
        print('Connection worked!')
        # Get roles
        result = cur.execute("SELECT * FROM dsi.zipcontents")
        zip = cur.fetchall()

        if result > 0:
            return render_template('displaytest.html', zip=zip)
        else:
            msg = 'No Data/Roles Found'
            return render_template('displaytest.html', msg=msg)

    # except  _mysql_exceptions.OperationalError as e:
    #     print('Failed connection')
    #     msg = 'Failed connection'
    #     return render_template('mysql.html', msg=msg)
    #     raise e
    finally:
        # Close connection
        #cur.close()
        pass
    
def makefile():
    file = open('testfile.txt','w')  
    file.write('Hello World') 
    file.write('This is our new text file') 
    file.write('and this is another line.') 
    file.write('Why? Because we can.') 
    file.close() 



# FILTERS THAT CAN BE USED
@app.template_filter('icon_fmt')
def icon_fmt(filename):
    i = 'fa-file-o'
    for icon, exts in icontypes.items():
        if filename.lower().split('.')[-1] in exts:
            i = icon
    return i




if __name__ == '__main__':
    app.secret_key='secret123435345351'
    app.run(debug=True)
