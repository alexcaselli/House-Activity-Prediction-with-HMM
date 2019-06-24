import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
import os
import plotly.graph_objs as go
import dash_dangerously_set_inner_html
from dash.dependencies import Input, Output



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
  html.H1('Mother Sensor', style={
        'textAlign': 'center'}),

  #Perfect button      
  html.Button(id='seat', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'pir', n_clicks=0,
    style = {'position':'relative', 'top':130, 'left':340, 'border': 'none'}),


  html.Div(id='result')
], style={"height" : "100vh", "background-image": 'url("https://i.ibb.co/Nj74KSS/Modelli540.png")', 'background-repeat': 'no-repeat', 'background-position': 'center'})



'''                              'layout': {
                                    'height': 800,
                                    'margin': {
                                        'l': 10, 'b': 20, 't': 0, 'r': 0
                                    }'''



#testing button callbacks, senza n_clicks lo esegue anche senza cliccare
@app.callback(Output('result', 'children'),
              [Input('seat', 'n_clicks'), Input('seat', 'name')])
def displayClick(n_clicks, btn):
    print(n_clicks)
    if(int(n_clicks) > 0):
      msg = 'spare time'
      
    else:
      msg = ''
    return msg


if __name__ == '__main__':
    app.run_server(debug=True)

