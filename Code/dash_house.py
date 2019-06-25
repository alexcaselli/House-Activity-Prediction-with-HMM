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
import csv



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

################### GLOBAL VARIABLE FOR ACTION OBSERVED AND MODEL ###################
actionObservedList = list()
activityName = list()
with open("./Model/HouseA.pkl", "rb") as fileA: 
   modelA = pickle.load(fileA)

with open("./Model/HouseB.pkl", "rb") as fileB: 
   modelB = pickle.load(fileB)


app.layout = html.Div([
  html.H1('Mother Sensor', style={
        'textAlign': 'center'}),
################### ADD BUTTON FOR HOME A ###################
  dcc.Tabs(id="tabs", children=[

    dcc.Tab(label='Casa A', children=[
      html.H3('Casa A', style={
        'textAlign': 'center'}),
     



      html.Div([

      # Basin Pir Bathroom
      html.Button(id='BasinPIRBathroom', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'BPB', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':200, 'left': 740, 'border': 'none'}),    
      
      # Bed Pressure Bedroom
      html.Button(id='BedPressureBedroom', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'BePBe', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':100, 'left':490, 'border': 'none'}),

      # Cabinet Magnetic Bathroom
      html.Button(id='CabinetMagneticBathroom', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'CMB', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':260, 'left':630, 'border': 'none'}),   

      # Cooktop PIR Kitchen
      html.Button(id='CooktopPIRKitchen', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'CPK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':167, 'left':15, 'border': 'none'}), 
      
      # Cupboard Magnetic Kitchen
      html.Button(id='CupboardMagneticKitchen', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'CMK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':275, 'left':-80, 'border': 'none'}), 

      # Fridge Magnetic Kitchen
      html.Button(id='FridgeMagneticKitchen', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'FMK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':35, 'left':-75, 'border': 'none'}), 

      # Maindoor Magnetic Entrance
      html.Button(id='MaindoorMagneticEntrance', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'MME', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':430, 'left':-550, 'border': 'none'}), 

      # Microwave Electric Kitchen 
      html.Button(id='MicrowaveElectricKitchen', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'MEK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':55, 'left':-385, 'border': 'none'}), 

      #Seat Pressure Living (before: 'top':130, 'left':340)      
      html.Button(id='SeatPressureLiving', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'SPL', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':135, 'left':-800, 'border': 'none'}),

      # Shower PIR Bathroom
      html.Button(id='ShowerPIRBathroom', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'SPB', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':48, 'left':-210, 'border': 'none'}),
      
      # Toaster Electric Kitchen
      html.Button(id='ToasterElectricKitchen', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'TEK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':197, 'left':-640, 'border': 'none'}), 

      # Toilet Flush Bathroom
      html.Button(id='ToiletFlushBathroom', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'TFB', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':175, 'left':-335, 'border': 'none'}),



     

      ], style={"height" : "600px", 'position':'relative', 'top':50 , 'left':'55vh', "background-image": 'url("https://i.ibb.co/g4ZqxYk/Modelli540-A.png")', 'background-repeat': 'no-repeat'}),
     html.Div(id='result', style={
        'textAlign': 'center'}),
       
    ]),





    #CASA B #########################################################################################
    dcc.Tab(label='CasaB', children=[

    html.H3('Casa B', style={
        'textAlign': 'center'}),
     



      html.Div([

      # Basin Pir Bathroom
      html.Button(id='BasinPIRBathroom_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'BPB', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':200, 'left': 740, 'border': 'none'}),    
      
      # Bed Pressure Bedroom
      html.Button(id='BedPressureBedroom_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'BePBe', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':100, 'left':490, 'border': 'none'}),

      # Cabinet Magnetic Bathroom
      html.Button(id='CabinetMagneticBathroom_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'CMB', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':260, 'left':630, 'border': 'none'}),   

      # Cooktop PIR Kitchen
      html.Button(id='CooktopPIRKitchen_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'CPK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':167, 'left':15, 'border': 'none'}), 
      
      # Cupboard Magnetic Kitchen
      html.Button(id='CupboardMagneticKitchen_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'CMK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':275, 'left':-80, 'border': 'none'}), 

      # Fridge Magnetic Kitchen
      html.Button(id='FridgeMagneticKitchen_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'FMK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':35, 'left':-75, 'border': 'none'}), 

      # Maindoor Magnetic Entrance
      html.Button(id='MaindoorMagneticEntrance_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'MME', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':430, 'left':-550, 'border': 'none'}), 

      # Microwave Electric Kitchen 
      html.Button(id='MicrowaveElectricKitchen_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'MEK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':55, 'left':-385, 'border': 'none'}), 

      #Seat Pressure Living (before: 'top':130, 'left':340)      
      html.Button(id='SeatPressureLiving_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'SPL', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':135, 'left':-800, 'border': 'none'}),

      # Shower PIR Bathroom
      html.Button(id='ShowerPIRBathroom_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'SPB', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':48, 'left':-210, 'border': 'none'}),
      
      # Toaster Electric Kitchen
      html.Button(id='ToasterElectricKitchen_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'TEK', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':197, 'left':-640, 'border': 'none'}), 

      # Toilet Flush Bathroom
      html.Button(id='ToiletFlushBathroom_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'TFB', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':175, 'left':-335, 'border': 'none'}),



     

      ], style={"height" : "600px", 'position':'relative', 'top':50 , 'left':'55vh', "background-image": 'url("https://i.ibb.co/g4ZqxYk/Modelli540-A.png")', 'background-repeat': 'no-repeat'}),
     html.Div(id='result_B', style={
        'textAlign': 'center'}),
    ]),

  ]),
  
])
################### RETRIVE ACTION FROM HOME A ###################
@app.callback(Output('result', 'children'),
              [Input('BasinPIRBathroom', 'n_clicks_timestamp'), Input('BedPressureBedroom', 'n_clicks_timestamp'), Input('CabinetMagneticBathroom', 'n_clicks_timestamp'), 
               Input('CooktopPIRKitchen', 'n_clicks_timestamp'), Input('CupboardMagneticKitchen', 'n_clicks_timestamp'), Input('FridgeMagneticKitchen', 'n_clicks_timestamp'), 
               Input('MaindoorMagneticEntrance', 'n_clicks_timestamp'), Input('MicrowaveElectricKitchen', 'n_clicks_timestamp'), Input('SeatPressureLiving', 'n_clicks_timestamp'),
               Input('ShowerPIRBathroom', 'n_clicks_timestamp'), Input('ToasterElectricKitchen', 'n_clicks_timestamp'), Input('ToiletFlushBathroom', 'n_clicks_timestamp')])

def displayClick(act0, act1, act2, act3, act4, act5, act6, act7, act8, act9, act10, act11):
    if sum(list((int(act0), int(act1), int(act2), int(act3), int(act4), int(act5), int(act6), int(act7), int(act8), int(act9), int(act10), int(act11)))) > 0:
      lastClicked = max(int(act0), int(act1), int(act2), int(act3), int(act4), int(act5), int(act6), int(act7), int(act8), int(act9), int(act10), int(act11))
      action = -1
      if int(act0) == lastClicked:
        print("ACTION 0")
        action = 0
      elif int(act1) == lastClicked:
        print("ACTION 1")
        action = 1
      elif int(act2) == lastClicked:
        print("ACTION 2")
        action = 2
      elif int(act3) == lastClicked:
        print("ACTION 3")
        action = 3
      elif int(act4) == lastClicked:
        print("ACTION 4")
        action = 4
      elif int(act5) == lastClicked:
        print("ACTION 5")
        action = 5
      elif int(act6) == lastClicked:
        print("ACTION 6")
        action = 6
      elif int(act7) == lastClicked:
        print("ACTION 7")
        action = 7
      elif int(act8) == lastClicked:
        print("ACTION 8")
        action = 8
      elif int(act9) == lastClicked:
        print("ACTION 9")
        action = 9
      elif int(act10) == lastClicked:
        print("ACTION 10")
        action = 10
      elif int(act11) == lastClicked:
        print("ACTION 11")
        action = 11

      if action == -1:
        print("This is a problem...")
      else:
        actionObservedList.append(action)
      
      print("ACTION OBSERVED: ", actionObservedList)
      print("INFERENCE: ", modelA.predict(np.array([actionObservedList]).T))
      translateNumberToActivity(actionObservedList, 'A')
      print("")

    if len(activityName) == 0:
      return html.Div([
          html.Div(activityName)   
      ])
    else:
      return html.Div([
          html.H2("Activity"),
          html.H4(activityName)

      ])

  

################### TRANSLATE NUMBER ACTION TO LITERAL ACTIVITY###################
def translateNumberToActivity(actionObservedList, house):
  activity = list()
  activityName.clear()

  if house=='A':

    lastActivityDistribution = list(modelA.predict_proba(np.array([actionObservedList]).T))[-1]

    with open('./Data/InferenceHomeA.csv', mode='w') as infereceA:
      infereceAWriter = csv.writer(infereceA, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      

      infereceAWriter.writerow(['Breakfast', 'Grooming', 'Leaving', "Lunch", "Showering", "Sleeping", "Snack", "Spare_Time/TV", "Toileting"])
      infereceAWriter.writerow([lastActivityDistribution[0], lastActivityDistribution[1], lastActivityDistribution[2], lastActivityDistribution[3], 
                                lastActivityDistribution[4], lastActivityDistribution[5], lastActivityDistribution[6], lastActivityDistribution[7], 
                                lastActivityDistribution[8]])

    activity = list(modelA.predict(np.array([actionObservedList]).T))
    for singleActivity in activity:
      if singleActivity == 0:
        activityName.append("Breakfast -> ")
      elif singleActivity == 1:
        activityName.append("Grooming -> ")
      elif singleActivity == 2:
        activityName.append("Leaving -> ")
      elif singleActivity == 3:
        activityName.append("Lunch -> ")
      elif singleActivity == 4:
        activityName.append("Showering -> ")
      elif singleActivity == 5:
        activityName.append("Sleeping -> ")
      elif singleActivity == 6:
        activityName.append("Snack -> ")
      elif singleActivity == 7:
        activityName.append("Spare_Time/TV -> ")
      elif singleActivity == 8:
        activityName.append("Toileting -> ")
      else:
        print("This is a problem...")
      
    print("ACTIVITY NAME: ", activityName)



################### RETRIVE ACTION FROM HOME B ###################
@app.callback(Output('result_B', 'children'),
              [Input('BasinPIRBathroom_B', 'n_clicks_timestamp'), Input('BedPressureBedroom_B', 'n_clicks_timestamp'), Input('CabinetMagneticBathroom_B', 'n_clicks_timestamp'), 
               Input('CooktopPIRKitchen_B', 'n_clicks_timestamp'), Input('CupboardMagneticKitchen_B', 'n_clicks_timestamp'), Input('FridgeMagneticKitchen_B', 'n_clicks_timestamp'), 
               Input('MaindoorMagneticEntrance_B', 'n_clicks_timestamp'), Input('MicrowaveElectricKitchen_B', 'n_clicks_timestamp'), Input('SeatPressureLiving_B', 'n_clicks_timestamp'),
               Input('ShowerPIRBathroom_B', 'n_clicks_timestamp'), Input('ToasterElectricKitchen_B', 'n_clicks_timestamp'), Input('ToiletFlushBathroom_B', 'n_clicks_timestamp')])

def displayClick(act0, act1, act2, act3, act4, act5, act6, act7, act8, act9, act10, act11):
    if sum(list((int(act0), int(act1), int(act2), int(act3), int(act4), int(act5), int(act6), int(act7), int(act8), int(act9), int(act10), int(act11)))) > 0:
      lastClicked = max(int(act0), int(act1), int(act2), int(act3), int(act4), int(act5), int(act6), int(act7), int(act8), int(act9), int(act10), int(act11))
      action = -1
      if int(act0) == lastClicked:
        print("ACTION 0")
        action = 0
      elif int(act1) == lastClicked:
        print("ACTION 1")
        action = 1
      elif int(act2) == lastClicked:
        print("ACTION 2")
        action = 2
      elif int(act3) == lastClicked:
        print("ACTION 3")
        action = 3
      elif int(act4) == lastClicked:
        print("ACTION 4")
        action = 4
      elif int(act5) == lastClicked:
        print("ACTION 5")
        action = 5
      elif int(act6) == lastClicked:
        print("ACTION 6")
        action = 6
      elif int(act7) == lastClicked:
        print("ACTION 7")
        action = 7
      elif int(act8) == lastClicked:
        print("ACTION 8")
        action = 8
      elif int(act9) == lastClicked:
        print("ACTION 9")
        action = 9
      elif int(act10) == lastClicked:
        print("ACTION 10")
        action = 10
      elif int(act11) == lastClicked:
        print("ACTION 11")
        action = 11

      if action == -1:
        print("This is a problem...")
      else:
        actionObservedList.append(action)
      
      print("ACTION OBSERVED: ", actionObservedList)
      print("INFERENCE: ", modelB.predict(np.array([actionObservedList]).T))
      translateNumberToActivity(actionObservedList, 'B')
      print("")

    if len(activityName) == 0:
      return html.Div([
          html.Div(activityName)   
      ])
    else:
      return html.Div([
          html.H2("Activity"),
          html.H4(activityName)

      ])



if __name__ == '__main__':
    app.run_server(debug=True)

# [0: 'Breakfast', 1: 'Grooming', 2: 'Leaving', 3: 'Lunch', 4: 'Showering',
#  5: 'Sleeping', 6: 'Snack', 7: 'Spare_Time/TV', 8: 'Toileting']

# ['0: BasinPIRBathroom', 1: 'BedPressureBedroom', 2: 'CabinetMagneticBathroom', 
#  3: 'CooktopPIRKitchen', 4: 'CupboardMagneticKitchen', 5: 'FridgeMagneticKitchen', 
#  6: 'MaindoorMagneticEntrance', 7: 'MicrowaveElectricKitchen', 8: 'SeatPressureLiving', 
#  9: 'ShowerPIRBathroom', 10: 'ToasterElectricKitchen', 11: 'ToiletFlushBathroom'] 




    '''print("CLICK SEAT: ", n_clicks1)
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
      msg = '''
