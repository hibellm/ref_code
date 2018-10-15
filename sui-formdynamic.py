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


# Vendors
@app.route('/vendors')
def vendors():
    # Create cursor
    cur = mysql.connection.cursor()
    # Get vendors
    result = cur.execute("SELECT * FROM vendors")
    vendors = cur.fetchall()

    if result > 0:
        return render_template('vendors.html', vendors=vendors)
    else:
        msg = 'No Vendors Found'
        return render_template('vendors.html', msg=msg)
    # Close connection
    cur.close()

#Single Vendor
@app.route('/vendor/<string:id>/')
def vendor(id):
    # Create cursor
    cur = mysql.connection.cursor()
    # Get vendor
    result = cur.execute("SELECT * FROM rwd_meta_mdh.accessroles WHERE roleaccessid = %s", [id])
    vendor = cur.fetchone()
    return render_template('vendor.html', vendor=vendor)





















@app.route('/formdynamic', methods=['GET','POST'])
def formdynamic():

    #TEST CONNECTION
    try:
        cur = mysql.connection.cursor()
        print('Connection worked!')
        
        # Get Roles for Dropdown
        result = cur.execute("SELECT table_schema FROM sys.schema_table_statistics group by table_schema")
        schemas = cur.fetchall()
        # print(eventsd)

        name2=''
        # if result > 0:
        #     if request.method == 'POST':
        #         name2=request.values.get("onesel")
        #         print('Single select is :'+str(name2))    
                
        #     #     name4=request.values.getlist("multsel")
        #     #     print('Multiple select is :'+str(name4))        
        #     #     for items in name4:
        #     #         print('Multiple select item is :'+(items))
        #     msg = 'Single select is :'+str(name2)
        #     return render_template('formdynamic.html', msg=msg,schemas=schemas)
        # else:
        #     msg = 'No Data/Roles Found'
        #     return render_template('formdynamic.html', msg=msg)  

        schema_name="%"
        print('Schema_name is '+schema_name)
        if request.method == 'POST': #The intial request to the page is a GET hence this if is not satisified which takes us directly to the else part
            schema_name = schemas[0].get(request.form.get('onesel')) # I have maintained a dictionary for short form of team names, this allows me to fetch them.
            print(schema_name)

            
            # docs = db.pdataGWX.find({"team_name":team_name},{"first_name":1,"second_name":1})

            result = cur.execute("SELECT table_name FROM sys.schema_table_statistics group by table_name where table_schema like %s",  'dsi')
            tables = cur.fetchall()
            print(str(tables))
            return render_template("formdynamic.html", schemas=request.form.get('onesel'), tables=tables)
        else:
            return render_template("formdynamic.html", schemas=request.form.get('onesel')) #During the initial request no variable is passed and the plain page is rendered, hence the second 'if' in the template page fails.
      
    finally:
        pass    

def stats():
    if request.method == 'POST': #The intial request to the page is a GET hence this if is not satisified which takes us directly to the else part
        schema_name = schema['table_schema'].get(request.form.get('onesel')) # I have maintained a dictionary for short form of team names, this allows me to fetch them.
        # docs = db.pdataGWX.find({"team_name":team_name},{"first_name":1,"second_name":1})
        return render_template("stats.html", schemas=request.form.get('onesel'), players=docs)
    else:
        return render_template("stats.html") #During the initial request no variable is passed and the plain page is rendered, hence the second 'if' in the template page fails.



if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
