#REFERENCE DBShortCode

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


@app.route('/formuserdetails', methods=['GET','POST'])
def formuserdetails():

    #TEST CONNECTION
    try:
        cur = mysql.connection.cursor()
        print('Connection worked!')
        
        # Get Dropdown
        result = cur.execute("SELECT table_schema,table_name FROM sys.schema_table_statistics group by table_schema, table_name")
        schemas = cur.fetchall()

        if request.method == 'POST':

            #SIMPLE TEXT BOX
            schemasel = request.values.getlist("onesel")

        return render_template("formuserdetails.html", schemas=schemas, schemasel=schemasel)  # During the initial request no variable is passed and the plain page is rendered, hence the second 'if' in the template page fails.
      
    finally:
        pass    
        
if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)

    
