from flask import Flask
from flask_apscheduler import APScheduler
 
import time
 
app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
 
@app.route('/')
def welcome():
    return 'Welcome to flask_apscheduler demo', 200
 
@app.route('/run-tasks')
def run_tasks():
    for i in range(10):
        app.apscheduler.add_job(func=scheduled_task, trigger='date', args=[i], id='j'+str(i))
 
    return 'Scheduled several long running tasks.', 200
 
def scheduled_task(task_id):
    for i in range(10):
        time.sleep(1)
        print('Task {} running iteration {}'.format(task_id, i))
         
app.run(port=8010)
