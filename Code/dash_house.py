import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
import os
import plotly.graph_objs as go
import dash_dangerously_set_inner_html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
  html.H1('Hello Dash', style={
        'textAlign': 'center'})

], style={"height" : "100vh", "background-image": 'url("https://i.ibb.co/f8HwzyQ/wall.jpg")', 'background-repeat': 'no-repeat', 'background-position': 'center'})


if __name__ == '__main__':
    app.run_server(debug=True)

