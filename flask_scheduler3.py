from flask import Flask
from flask_apscheduler import APScheduler
import datetime as dt
import os

# set configuration values
class Config:
    SCHEDULER_API_ENABLED = True

# create app
app = Flask(__name__)
app.config.from_object(Config())

# initialize scheduler
scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:

# interval example
@scheduler.task('interval', id='do_job_1', seconds=30, misfire_grace_time=900)
def job1():
    print(f'Job 1 executed {dt.datetime.now()}')
    os.system('python code2run.py')
    print(f'Job 1 executed {dt.datetime.now()}')
    


# cron examples
# EVERY MINUTE
@scheduler.task('cron', id='do_job_2', minute='*')
def job2():
    print(f'Job 2 executed {dt.datetime.now()}')

# EVERY 3 MINS
@scheduler.task('cron', id='do_job_3', minute='*/3')
def job2():
    print(f'Job 3 executed {dt.datetime.now()}')

# scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()


if __name__ == '__main__':
    app.run(port=8010)
