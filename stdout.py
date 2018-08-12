import execute as exc
import time
import subprocess
import os
from flask import render_template, Flask, Response, flash, redirect, url_for, request, session, logging
from jinja2 import Environment 
# http://jinja.pocoo.org/docs/2.10/extensions/#jinja-extensions
from jinja2.loaders import FileSystemLoader

app = Flask(__name__)
 
# assume that your homepage shows the console output.
@app.route('/')
def home():
    output, errors = exc.execute("help",".")
    return render_template('stdout.html', console_gave = [output, errors])
 
@app.route('/yield')
def index():
    def inner():
        for x in range(20):
            time.sleep(0.1)
            yield '%s<br/>\n' % x
            
    env = Environment(loader=FileSystemLoader('templates'),extensions=['jinja2.ext.with_','jinja2.ext.loopcontrols'])
    tmpl = env.get_template('stdout.html')
    return Response(tmpl.generate(result=inner()))
    
# PRINTS TO A SEGMENT IN THE STDOUT.HTML    
@app.route('/yield2')
def index2():
    def inner2():    
        proc = subprocess.Popen(
            ['python','code2run.py'],             #call something with a lot of output so we can see it            
            universal_newlines=True,
            stdout=subprocess.PIPE
        )

        for line in iter(proc.stdout.readline,''):
            time.sleep(0.1)                           # Don't need this just shows the text streaming
            yield line.rstrip() + '<br/>\n'

    env = Environment(loader=FileSystemLoader('templates'))
    tmpl = env.get_template('stdout.html')
    return Response(tmpl.generate(result2=inner2()))            

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
