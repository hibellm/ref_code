#REFERENCE DBShortCode

# TO USE SEMANTIC-UI AND CONNECTION TO DATABASES

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from data import Vendors
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, RadioField, BooleanField, validators
from wtforms.validators import DataRequired
from passlib.hash import sha256_crypt
from functools import wraps
from datetime import datetime, date, time

app = Flask(__name__)


@app.route('/mysql')
def mysql():
    # Config MySQL
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'myflaskapp'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    # init MYSQL
    mysql = MySQL(app)

   #TEST CONNECTION
    try:
        cur = mysql.connection.cursor()
        print('Connection worked!')
        # Get roles
        result = cur.execute("SELECT * FROM rwd_meta_mdh.event_log")
        events = cur.fetchall()

        # Get Roles for Dropdown
        result = cur.execute("SELECT * FROM rwd_meta_mdh.event_log group by eventtype")
        eventsd = cur.fetchall()
        print(result)

        if result > 0:
            return render_template('mysql.html', events=events, eventsd=eventsd)
        else:
            msg = 'No Data/Roles Found'
            return render_template('mysql.html', msg=msg)

    # except  _mysql_exceptions.OperationalError as e:
    #     print('Failed connection')
    #     msg = 'Failed connection'
    #     return render_template('mysql.html', msg=msg)
    #     raise e
    finally:
        # Close connection
        #cur.close()
        pass

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=False)
