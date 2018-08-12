# Reference https://dash.plot.ly/getting-started

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()


app.css.append_css({"external_url": "https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.3.2/semantic.min.css"})

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


app.layout = html.Div(className='jumbotron text-center', id='headingt',style={'backgroundColor': colors['background']} )

app.layout = html.Div(className='ui segment', id='graph', children=[
    html.H3(children='Dash: A web application framework for Python.'        
    ),

   dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.secret_key='secret123'    
    app.run_server(port=5000,debug=True)


"""

html.Div([
        html.Div('', className='jumbotron  text-center',
                children=[html.H1('Dash: A web application framework for Python.')],
                ),
        html.P('Example P', className='my-class', id='my-p-element')
         ],className='container')

"""