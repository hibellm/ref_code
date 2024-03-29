#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
CREATED    : 15JUL2019
AUTHOR     : HIBELLM
DESCRIPTION: Template for a Flask application
"""


from flask import Flask, make_response, request, session, render_template, send_file, Response
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

upload_folder = '/path/to/the/uploads'
allowed_ext = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


# APP settings
app = Flask(__name__, static_url_path='/assets', static_folder='assets')
app.config['UPLOAD_FOLDER'] = upload_folder
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/markdown')
def markdown():
    return render_template('markdown.html')


# ERROR HANDLING
@app.errorhandler(404)
def page_not_found(error):
    msg = f"why cant I find the page you want - report sent to admins"
    return render_template('page_not_found.html', msg=msg), 404


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(port=8000, threaded=True, debug=True)

