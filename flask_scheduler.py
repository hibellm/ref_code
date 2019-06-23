#!/usr/bin/python3
""" Demonstrating APScheduler feature for small Flask App. """

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template
import pickle
import datetime


def sensor():
    """ Function for test purposes. """
    sensor = f"Scheduler is alive! {datetime.datetime.now()}"
    print(f"Scheduler is alive! {datetime.datetime.now()}")
    pickle.dump(sensor, open("save.sensor", "wb"))


sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor, 'interval', seconds=60)
sched.start()

app = Flask(__name__)


@app.route("/home")
def home():
    sensor = ""
    try:
        sensor = pickle.load(open("save.sensor", "rb"))
    except:
        pass

    return render_template('flaskscheduler.html', sensor=sensor)
    # return f"Welcome Home :) ! {sensor}"


if __name__ == "__main__":
    app.run()
