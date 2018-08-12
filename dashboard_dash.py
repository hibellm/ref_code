import pandas as pd
# from definitions import ROOT_DIR
import os
import dash
# import dash_wordcloud
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objs as go

ROOT_DIR='static'

data_phones_csv = os.path.join(ROOT_DIR, 'data/cell_phone_total.csv')
data_phones = pd.read_csv(data_phones_csv, delimiter=';')

europe = ['Poland', 'Portugal', 'Italy', 'Spain', 'Slovenia', 'Germany', 'Ireland', 'Greece', 'France',
          'Sweden', 'Denmark', 'Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Estonia',
          'Finland']

countries_eu = data_phones.loc[data_phones['Country'].isin(europe)]
values_1980 = countries_eu.ix[:, '1980'].values
country = countries_eu.ix[:, 'Country'].values
columns = list(countries_eu.columns)
years = columns[1:]
years = [int(i) for i in years]


def word_size(variable):
    scale_factor = 300
    word_size = np.sqrt(variable / np.pi) / scale_factor
    min_size = 0
    return word_size


def generate_wordcloud_data(year):
    default_list = []
    values_year = countries_eu.ix[:, str(year)].values
    w_size = word_size(values_year)
    for i in range(len(country)):
        word_element = (country[i], w_size[i])
        default_list.append(word_element)
    return default_list



def process_data_list(value):
    data_list = generate_wordcloud_data(value)
    return data_list


default_list = generate_wordcloud_data(1980)

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(
        children='Dash example',
        style={
            'textAlign': 'center'
        }
    ),
    html.Div([
        dcc.Slider(
            id='years-slider',
            min=min(years),
            max=max(years),
            step=1,
            marks={str(year): str(year) for year in years},
            included=False,
            value=min(years),
        ),
    ], style={'width': 1200, 'margin': 25})
    ,
    html.Div(
        [
            html.Div([
                html.Div([
                    html.P('Total mobile subscriptions in EU countries in year {0}'.format(min(years)),
                           id='barchart-title',
                           style={'fontWeight': 600, 'textAlign': 'center'})
                ]),
                dcc.Graph(
                    id='bar_chart',
                    figure={
                        'data': [
                            {'x': country,
                             'y': values_1980,
                             'type': 'bar',
                             'name': country}
                        ]
                    })
            ],
                className='eight columns',
                style={'margin-top': '20'})
            ,
            html.Div([
                dash_wordcloud.Wordcloud(id='wc',
                                         #  list = default_list,
                                         style=dict(height='200px', width='200px'),
                                         options=dict(color='random-light',
                                                      size=2,
                                                      backgroundColor='white'))
            ],
                className='four columns',
                style={'margin-top': '20'}),
        ],
        className='row'
    ),

],
    className='ten columns offset-by-one')


@app.callback(
    Output('bar_chart', 'figure'),
    [Input('years-slider', 'value')])
def update_bar_chart(year):
    year = str(year)
    data = [
        {'x': country,
         'y': countries_eu.ix[:, year].values,
         'type': 'bar'}
    ]
    figure = dict(data=data)
    return figure


@app.callback(
    Output('barchart-title', 'children'),
    [Input('years-slider', 'value')])
def update_bar_title(year):
    return 'Total mobile subscriptions in EU countries in year {0}'.format(year)


@app.callback(
    Output('wc', 'list'),
    [Input('years-slider', 'value')])
def update_wordcloud(year):
    return process_data_list(year)



if __name__ == '__main__':
    app.run_server(port=5000,debug=True)
