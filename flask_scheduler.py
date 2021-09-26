#!/usr/bin/python3
""" Demonstrating APScheduler feature for small Flask App. """

from flask import Flask, render_template
import pickle
import datetime as dt
import queue
import threading
import time
from pymongo import MongoClient  # Database connector
from bson.objectid import ObjectId  # For ObjectId to work
from bson.son import SON
import bson
import json


client = MongoClient('localhost', 27017)    # Configure the connection to the database
db = client.mdh       # Select the database
vendors = db.vendors  # Select the collection

dsidb = client.dsi    # Select the database
dsido = dsidb.DataObject
dsidv = dsidb.DeliverObject
dsidict = dsidb.dictionary
dsistudy = dsidb.StudyMetadata
dsitrain = dsidb.train


def every_1_min():
    """Every min"""
    while True:
         print(f"Every min - Scheduler is alive! {dt.datetime.now()}")
         dsitrain.insert_one({"test_modified": dt.datetime.utcnow()})
         time.sleep(60)
 

def sensor():
    """ Function for test purposes. """
    sensor = f"Scheduler is alive! {dt.datetime.now()}"
    print(f"Scheduler is alive! {dt.datetime.now()}")
    pickle.dump(sensor, open("save.sensor", "wb"))


t1 = threading.Thread(target=every_1_min)
t2 = threading.Thread(target=sensor)

t1.start()
t2.start()


app = Flask(__name__, static_url_path='/assets', static_folder='assets')


@app.route('/home')
def home():
    """sensor"""
    sensor = ""
    try:
        sensor = pickle.load(open("save.sensor", "rb"))
    except:
        pass

    return render_template('flaskscheduler.html', sensor=sensor)
    # return f"Welcome Home :) ! {sensor}"


if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run(port=8010,  threaded=True, debug=True)
