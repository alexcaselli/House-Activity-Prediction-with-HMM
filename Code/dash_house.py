import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
import os
import plotly.graph_objs as go
import dash_dangerously_set_inner_html
from dash.dependencies import Input, Output
from hmmlearn import hmm
import pickle
import numpy as np



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

actionObservedList = list()
with open("./Model/HouseA.pkl", "rb") as fileA: 
   modelA = pickle.load(fileA)


app.layout = html.Div([

  dcc.Tabs(id="tabs", children=[
    dcc.Tab(label='CasaA', children=[

      html.H1('Mother Sensor', style={
        'textAlign': 'center'}),

      html.Div([

        # Basin Pir Bathroom
      html.Button(id='BasinPIRBathroom', children=[html.Img(src='https://img.icons8.com/color/96/000000/xbox-x.png')], name = 'BPB', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':'10px', 'left': '0px', 'border': 'none'}),    
      
      # Bed Pressure Bedroom
      html.Button(id='BedPressureBedroom', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'BePBe', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':40, 'left':0, 'border': 'none'}), 

      # Cabinet Magnetic Bathroom
      html.Button(id='CabinetMagneticBathroom', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'CMB', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':70, 'left':0, 'border': 'none'}),  

      # Cooktop PIR Kitchen
      html.Button(id='CooktopPIRKitchen', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'CPK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':100, 'left':0, 'border': 'none'}), 

      # Cupboard Magnetic Kitchen
      html.Button(id='CupboardMagneticKitchen', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'CMK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':130, 'left':0, 'border': 'none'}), 

      # Fridge Magnetic Kitchen  
      html.Button(id='FridgeMagneticKitchen', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'FMC', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':160, 'left':0, 'border': 'none'}),

      # Maindoor Magnetic Entrance
      html.Button(id='MaindoorMagneticEntrance', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'MME', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':190, 'left':0, 'border': 'none'}), 

      # Microwave Electric Kitchen
      html.Button(id='MicrowaveElectricKitchen', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'MEK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':220, 'left':0, 'border': 'none'}), 

      #Seat Pressure Living (before: 'top':130, 'left':340)      
      html.Button(id='SeatPressureLiving', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'SPL', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':250, 'left':0, 'border': 'none'}),

      # Shower PIR Bathroom
      html.Button(id='ShowerPIRBathroom', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'SPB', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':270, 'left':0, 'border': 'none'}), 

      # Toaster Electric Kitchen
      html.Button(id='ToasterElectricKitchen', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'TEK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':300, 'left':0, 'border': 'none'}), 

      # Toilet Flush Bathroom
      html.Button(id='ToiletFlushBathroom', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'TFB', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':330, 'left':0, 'border': 'none'}), 









      html.Div(id='result')

      ], style={"height" : "1000px", 'position':'relative', 'top':50 , 'left':'65vh', "background-image": 'url("https://i.ibb.co/Nj74KSS/Modelli648.png")', 'background-repeat': 'no-repeat'}),

      
    ]),
    dcc.Tab(label='CasaB', children=[
    ]),

  ]),
  
])
#'background-position': 'center'
#testing button callbacks, senza n_clicks lo esegue anche senza cliccare
@app.callback(Output('result', 'children'),
              [Input('SeatPressureLiving', 'n_clicks_timestamp'), Input('FridgeMagneticKitchen', 'n_clicks_timestamp')])

def displayClick(n_clicks1, n_clicks2):
    print("CLICK SEAT: ", n_clicks1)
    print("CLICK FridgeMagneticKitchen: ", n_clicks2)
    print("")
    if(int(n_clicks1) + int(n_clicks2) > 0):
      if int(n_clicks1) == max(int(n_clicks2), int(n_clicks1)):
        print("SOFA")
        actionObservedList.append(8)
        # print(actionObservedList)
      elif int(n_clicks2) == max(int(n_clicks2), int(n_clicks1)):
        print("FRIDGE")
        actionObservedList.append(5)

      # msg = 'spare time'
      print("MODEL INFERENCE: ", modelA.predict(np.array([actionObservedList]).T))
      print("")
      
      msg = ''
    else:
      msg = ''
    return msg


if __name__ == '__main__':
    app.run_server(debug=True)



# [0: 'Breakfast', 1: 'Grooming', 2: 'Leaving', 3: 'Lunch', 4: 'Showering',
#  5: 'Sleeping', 6: 'Snack', 7: 'Spare_Time/TV', 8: 'Toileting']

# ['0: BasinPIRBathroom', 1: 'BedPressureBedroom', 2: 'CabinetMagneticBathroom', 
#  3: 'CooktopPIRKitchen', 4: 'CupboardMagneticKitchen', 5: 'FridgeMagneticKitchen', 
#  6: 'MaindoorMagneticEntrance', 7: 'MicrowaveElectricKitchen', 8: 'SeatPressureLiving', 
#  9: 'ShowerPIRBathroom', 10: 'ToasterElectricKitchen', 11: 'ToiletFlushBathroom'] 
