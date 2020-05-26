#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""
CREATED    :
AUTHOR     :
DESCRIPTION:
"""

# """
# class to create json files with
# parent/child hierarchy from a pandas
# DataFrame
# example use of the json file would
# be in a sunburst plot
# """
#
# import os, sys
# import pandas as pd
# import json
#
# class jsonMaker(object):
#
#     def __init__(self, sql='', df='', jsonfile=''):
#         self.conn = ''
#         self.servername = ''
#         self.dbname = ''
#         self.sql = sql
#         self.df = df
#         self.jsonfile = jsonfile
#
#     def sqlconn(self):
#         """
#         example method to connect to a SQL server
#         uses pandas to read the return query directly
#         into a DataFrame
#         """
#
#         import pyodbc
#
#         conn = pyodbc.connect("DRIVER=SQL Server; \
#                            SERVER={0}; \
#                            database={1}; \
#                            Trusted_Connection=yes" \
#                            .format(self.servername,
#                                    self.dbname))
#
#         self.conn = conn
#
#         self.df = pd.read_sql(self.sql, conn)
#
#     def writeJSON(self, df=None, jsonfile=None):
#         """
#         writeJSON - used to create a json file from a pandas dataframe
#         for use in a sunburst plot.
#         Parameters
#         -----------------
#         df: pandas dataframe, can contain multiple columns, beginning
#         with most generic classification first, down to most specific
#         classification (e.g. state, office, section, employee) - last
#         column should be numerical value used to calculate proportion
#         for each class
#         jsonfile: string, name of json output file
#         Modified from:
#         http://stackoverflow.com/questions/19317115/convert-flat-json-file-to-hierarchical-json-data-like-flare-json-d3-example-fil?rq=1
#         """
#
#         if not isinstance(df, pd.DataFrame):
#             df = self.df
#         if jsonfile == None:
#             jsonfile = self.jsonfile
#
#         dataStructure = {'name':'', 'children': []}
#
#         for data in df.iterrows():
#
#             current = dataStructure
#             depthCursor = current['children']
#             for i, item in enumerate(data[1][:-2]):
#                 idx = None
#                 j = None
#                 for j, c in enumerate(depthCursor):
#                     if item in c.values():
#                         idx = j
#                 if idx == None:
#                     depthCursor.append({'name':item, 'children':[]})
#                     idx = len(depthCursor) - 1
#
#                 depthCursor = depthCursor[idx]['children']
#                 if i == len(data[1])-3:
#                     depthCursor.append({'name':'{}'.format(data[1][-2]),
#                                         'size': data[1][-1]})
#
#                 current = depthCursor
#
#         f = open(jsonfile, 'w')
#         json.dump(dataStructure, f, indent=4)
#         f.close()
#
#
# import pandas as pd
# import df2json as dj
#
# def blackhills():
#     df = pd.read_csv(os.path.join(ROOT_DIR, 'data/blackHillsBudget.csv'))
#     jm = dj.jsonMaker(sql='', jsonfile='blackhills.json')
#     jm.writeJSON(df=df)
#
# blackhills()


# NOW THE APP


from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
#from data import Vendors
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, RadioField, BooleanField, validators
from wtforms.validators import DataRequired
from passlib.hash import sha256_crypt
from functools import wraps
from datetime import datetime, date, time

app = Flask(__name__)

ROOT_DIR = 'static'

import plotly
import plotly.graph_objs as go
import pandas as pd
plotly.__version__


df1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/sunburst-coffee-flavors-complete.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/coffee-flavors.csv')

trace1 = go.Sunburst(
    ids=df1.ids,
    labels=df1.labels,
    parents=df1.parents,
    domain=dict(column=0)
)

trace2 = go.Sunburst(
    ids=df2.ids,
    labels=df2.labels,
    parents=df2.parents,
    domain=dict(column=1),
    maxdepth=2
)

layout = go.Layout(
    grid=go.layout.Grid(columns=2, rows=1),
    margin=go.layout.Margin(t=0, l=0, r=0, b=0),
    sunburstcolorway=[
    "#636efa", "#EF553B", "#00cc96", "#ab63fa", "#19d3f3",
    "#e763fa", "#FECB52", "#FFA15A", "#FF6692", "#B6E880"
  ],
    extendsunburstcolors=True
)

data = [trace1, trace2]

fig = go.Figure(data, layout)

plotly.iplot(fig, filename='large_number_of_slices')

@app.route('/sui_d3sunburst', methods=['GET', 'POST'])
def sui_d3sunburst():

    return render_template('sui-d3sunburst.html')

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)

