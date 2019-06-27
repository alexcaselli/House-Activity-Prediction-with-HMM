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
actionObservedList_B = list()
activityName_B = list()


app.layout = html.Div([
  html.H1('Mother Sensor', style={
        'textAlign': 'center'}),
################### ADD BUTTON FOR HOME A ###################
  dcc.Tabs(id="tabs", children=[

    dcc.Tab(label='House A', children=[
      html.H3('House A', style={
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

    html.Div([
      dcc.Dropdown(
    options=[
        {'label': 'Basin PIR Bathroom', 'value': '0'},
        {'label': 'Bed Pressure Bedroom', 'value': '1'},
        {'label': 'Cabinet Magnetic Bathroom', 'value': '2'}, 
        {'label': 'Cooktop PIR Kitchen', 'value': '3'},
        {'label': 'Cupboard Magnetic Kitchen', 'value': '4'},
        {'label': 'Fridge Magnetic Kitchen', 'value': '5'}, 
        {'label': 'Maindoor Magnetic Entrance', 'value': '6'},
        {'label': 'Microwave Electric Kitchen', 'value': '7'},
        {'label': 'Seat Pressure Living', 'value': '8'}, 
        {'label': 'Shower PIR Bathroom', 'value': '9'},
        {'label': 'ToasterE lectric Kitchen', 'value': '10'},
        {'label': 'Toilet Flush Bathroom', 'value': '11'}, 
    ],
    value=[],
    multi=True
)  
    ]),
      
       
    ]),

# [0: 'Breakfast', 1: 'Grooming', 2: 'Leaving', 3: 'Lunch', 4: 'Showering',
#  5: 'Sleeping', 6: 'Snack', 7: 'Spare_Time/TV', 8: 'Toileting']

# ['0: BasinPIRBathroom', 1: 'BedPressureBedroom', 2: 'CabinetMagneticBathroom', 
#  3: 'CooktopPIRKitchen', 4: 'CupboardMagneticKitchen', 5: 'FridgeMagneticKitchen', 
#  6: 'MaindoorMagneticEntrance', 7: 'MicrowaveElectricKitchen', 8: 'SeatPressureLiving', 
#  9: 'ShowerPIRBathroom', 10: 'ToasterElectricKitchen', 11: 'ToiletFlushBathroom'] 



    ################### ADD BUTTON FOR HOME B ###################
    dcc.Tab(label='House B', children=[

    html.H3('House B', style={
        'textAlign': 'center'}),
     
# 0: 'BasinPIRBathroom_B', 1:'BedPressureBedroom_B', 2:'CupboardMagneticKitchen_B', '3: DoorPIRBedroom_B', 4: 'DoorPIRKitchen_B', 5: 'DoorPIRLiving_B', 6: 'FridgeMagneticKitchen_B',
# 7: 'MaindoorMagneticEntrance_B', 8: 'MicrowaveElectricKitchen_B', 9: 'SeatPressureLiving_B', 10: 'ShowerPIRBathroom_B', '11: ToiletFlushBathroom_B']

# 0: 'Breakfast', 1: 'Dinner', 2: 'Grooming', 3: 'Leaving', 4: 'Lunch', 5: 'Showering', 6: 'Sleeping', 7: 'Snack', 8: 'Spare_Time/TV', 9: 'Toileting']


      html.Div([

      # Basin Pir Bathroom
      html.Button(id='BasinPIRBathroom_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'BPB_B', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':200, 'left': 740, 'border': 'none'}),    
      
      # Bed Pressure Bedroom
      html.Button(id='BedPressureBedroom_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'BePBe_B', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':100, 'left':490, 'border': 'none'}),

      # Cupboard Magnetic Kitchen
      html.Button(id='CupboardMagneticKitchen_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'CMK_B', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':275, 'left':140, 'border': 'none'}), 

      # Door PIR RBedroom
      html.Button(id='DoorPIRBedroom_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'DPB_B', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':320, 'left':295, 'border': 'none'}),   

      # Door PIR Kitchen
      html.Button(id='DoorPIRKitchen_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'DPK_B', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':320, 'left':0, 'border': 'none'}),  
      
      # Door PIR Living
      html.Button(id='DoorPIRLiving_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'DPL_B', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':320, 'left':-395, 'border': 'none'}),  

      # Fridge Magnetic Kitchen
      html.Button(id='FridgeMagneticKitchen_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'FMK_B', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':35, 'left':-183, 'border': 'none'}),  

       # Maindoor Magnetic Entrance
      html.Button(id='MaindoorMagneticEntrance_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'MME_B', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':430, 'left':-660, 'border': 'none'}), 

       # Microwave Electric Kitchen 
      html.Button(id='MicrowaveElectricKitchen_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'MEK_B', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':55, 'left':-495, 'border': 'none'}), 

      #Seat Pressure Living (before: 'top':130, 'left':340)      
      html.Button(id='SeatPressureLiving_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'SPL_B', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':135, 'left':-908, 'border': 'none'}),

      # Shower PIR Bathroom (Left -108 rispetto a casa A)
      html.Button(id='ShowerPIRBathroom_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'SPB_B', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':48, 'left':-318, 'border': 'none'}),

       # Toilet Flush Bathroom
      html.Button(id='ToiletFlushBathroom_B', children=[html.Img(src='https://img.icons8.com/color/48/000000/xbox-x.png')], name = 'TFB_B', n_clicks_timestamp=0,
        style = {'position':'relative', 'top':175, 'left':-335, 'border': 'none'}),



     

      ], style={"height" : "600px", 'position':'relative', 'top':50 , 'left':'55vh', "background-image": 'url("https://i.ibb.co/g4ZqxYk/Modelli540-A.png")', 'background-repeat': 'no-repeat'}),
     html.Div(id='result_B', style={
        'textAlign': 'center'}),
    ]),

  ]),

# [0: 'Breakfast', 1: 'Grooming', 2: 'Leaving', 3: 'Lunch', 4: 'Showering',
#  5: 'Sleeping', 6: 'Snack', 7: 'Spare_Time/TV', 8: 'Toileting']

# ['0: BasinPIRBathroom', 1: 'BedPressureBedroom', 2: 'CabinetMagneticBathroom', 
#  3: 'CooktopPIRKitchen', 4: 'CupboardMagneticKitchen', 5: 'FridgeMagneticKitchen', 
#  6: 'MaindoorMagneticEntrance', 7: 'MicrowaveElectricKitchen', 8: 'SeatPressureLiving', 
#  9: 'ShowerPIRBathroom', 10: 'ToasterElectricKitchen', 11: 'ToiletFlushBathroom'] 
  
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
      distribution_A = pd.read_csv('./Data/InferenceHomeA.csv')
      top3Activity = dict()
      index = 0
      activityTake = list()

      while index < 3:
        maxValue = 0
        maxActivity = ""
        for activityDistribution in distribution_A:
          if distribution_A[activityDistribution][0] > maxValue:
            if distribution_A[activityDistribution].name not in activityTake:
              maxValue = distribution_A[activityDistribution][0]
              maxActivity = distribution_A[activityDistribution].name
        print(maxValue)
        print(maxActivity)
        activityTake.append(maxActivity)
        top3Activity[maxActivity] = maxValue
        index += 1
      
      print(activityTake)
      print(top3Activity)
      print("")

      with open('./Data/MAXInferenceHomeA.csv', mode='w') as infereceA:
        infereceAWriter = csv.writer(infereceA, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      

        infereceAWriter.writerow(['A0', 'A1', 'A2'])
        infereceAWriter.writerow([top3Activity[activityTake[0]], top3Activity[activityTake[1]], top3Activity[activityTake[2]]])

      distribution_A = pd.read_csv('./Data/MAXInferenceHomeA.csv')
      
      return html.Div([
          html.H2("Activity"),
          html.H4(activityName)
      ]), html.Div([
            dcc.Graph(
            id='LastActivityDistribution',
                    figure={
                        'data': [
                            {'x': str(activityTake[0]), 'y': distribution_A.A0,
                                'type': 'bar', 'name': str(activityTake[0])},
                            {'x': str(activityTake[1]), 'y': distribution_A.A1,
                                'type': 'bar', 'name': str(activityTake[1])},
                            {'x': str(activityTake[2]), 'y': distribution_A.A2,
                                'type': 'bar', 'name': str(activityTake[2])},],
                        'layout': {
                    'title': 'Last Activity Distribution'
                        }
                    }
                ),

      ])

  

################### TRANSLATE NUMBER ACTVITY TO LITERAL ACTIVITY###################
def translateNumberToActivity(actionObservedList, house):
  activity = list()
  activity_B = list()
  activityName.clear()
  activityName_B.clear()

  if house=='A':

    lastActivityDistribution = list(modelA.predict_proba(np.array([actionObservedList]).T))[-1]

    with open('./Data/InferenceHomeA.csv', mode='w') as infereceA:
      infereceAWriter = csv.writer(infereceA, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      

      infereceAWriter.writerow(['Breakfast', 'Grooming', 'Leaving', "Lunch", "Showering", "Sleeping", "Snack", "Spare_Time_TV", "Toileting"])
      infereceAWriter.writerow([lastActivityDistribution[0], lastActivityDistribution[1], lastActivityDistribution[2], lastActivityDistribution[3], 
                                lastActivityDistribution[4], lastActivityDistribution[5], lastActivityDistribution[6], lastActivityDistribution[7], 
                                lastActivityDistribution[8]])

    # activity = np.where(lastActivityDistribution == np.amax(lastActivityDistribution))
    # activity = list(modelA.predict(np.array([actionObservedList]).T))
    activity = list(modelA.predict_proba(np.array([actionObservedList]).T))
    # print(activity)
    # print("DIOCANE: ", activity[-1])
    # print("MADONNA TROIA: ", type(lastActivityDistribution))
    for distribution in activity:
      singleActivity = np.where(distribution == np.amax(distribution))
      singleActivity = singleActivity[0]
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
        activityName.append("Spare Time/TV -> ")
      elif singleActivity == 8:
        activityName.append("Toileting -> ")
      else:
        print("This is a problem...")
      
    print("ACTIVITY NAME: ", activityName)
  #--------------------CASA B----------------------------
  ################################################################
  else:
    lastActivityDistribution = list(modelB.predict_proba(np.array([actionObservedList]).T))[-1]

    with open('./Data/InferenceHomeB.csv', mode='w') as infereceB:
      infereceBWriter = csv.writer(infereceB, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      

      infereceBWriter.writerow(['Breakfast', 'Dinner', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting'])
      infereceBWriter.writerow([lastActivityDistribution[0], lastActivityDistribution[1], lastActivityDistribution[2], lastActivityDistribution[3], 
                                lastActivityDistribution[4], lastActivityDistribution[5], lastActivityDistribution[6], lastActivityDistribution[7], 
                                lastActivityDistribution[8], lastActivityDistribution[9]])

    # activity_B = list(modelB.predict(np.array([actionObservedList]).T))
    activity_B = list(modelB.predict_proba(np.array([actionObservedList]).T))
    for distribution in activity_B:
      singleActivity = np.where(distribution == np.amax(distribution))
      singleActivity = singleActivity[0]
      # print('Ho trovato:' + str(singleActivity))
      if singleActivity == 0:
        activityName_B.append("Breakfast -> ")
      elif singleActivity == 1:
        activityName_B.append("Dinner -> ")
      elif singleActivity == 2:
        activityName_B.append("Grooming -> ")
      elif singleActivity == 3:
        activityName_B.append("Leaving -> ")
      elif singleActivity == 4:
        activityName_B.append("Lunch -> ")
      elif singleActivity == 5:
        activityName_B.append("Showering -> ")
      elif singleActivity == 6:
        activityName_B.append("Sleeping -> ")
      elif singleActivity == 7:
        activityName_B.append("Snack -> ")
      elif singleActivity == 8:
        activityName_B.append("Spare Time/TV -> ")
      elif singleActivity == 9:
        activityName_B.append("Toileting -> ")
      else:
        print("This is a problem...")
      
    print("ACTIVITY NAME: ", activityName_B)




################### RETRIVE ACTION FROM HOME B ###################
@app.callback(Output('result_B', 'children'),
              [Input('BasinPIRBathroom_B', 'n_clicks_timestamp'), Input('BedPressureBedroom_B', 'n_clicks_timestamp'), Input('CupboardMagneticKitchen_B', 'n_clicks_timestamp'), Input('DoorPIRBedroom_B', 'n_clicks_timestamp'),
               Input('DoorPIRKitchen_B', 'n_clicks_timestamp'), Input('DoorPIRLiving_B', 'n_clicks_timestamp'), Input('FridgeMagneticKitchen_B', 'n_clicks_timestamp'), 
               Input('MaindoorMagneticEntrance_B', 'n_clicks_timestamp'), Input('MicrowaveElectricKitchen_B', 'n_clicks_timestamp'), Input('SeatPressureLiving_B', 'n_clicks_timestamp'),
               Input('ShowerPIRBathroom_B', 'n_clicks_timestamp'), Input('ToiletFlushBathroom_B', 'n_clicks_timestamp')])

def displayClick2(act0, act1, act2, act3, act4, act5, act6, act7, act8, act9, act10, act11):
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
        actionObservedList_B.append(action)
      
      print("ACTION OBSERVED: ", actionObservedList_B)
      print("INFERENCE: ", modelB.predict(np.array([actionObservedList_B]).T))
      translateNumberToActivity(actionObservedList_B, 'B')
      print("")
    if len(activityName_B) == 0:
      return html.Div([
          html.Div(activityName_B)   
      ])
    else:
      distribution_B = pd.read_csv('./Data/InferenceHomeB.csv')
      top3Activity = dict()
      index = 0
      activityTake = list()

      while index < 3:
        maxValue = 0
        maxActivity = ""
        for activityDistribution in distribution_B:
          if distribution_B[activityDistribution][0] > maxValue:
            if distribution_B[activityDistribution].name not in activityTake:
              maxValue = distribution_B[activityDistribution][0]
              maxActivity = distribution_B[activityDistribution].name
        print(maxValue)
        print(maxActivity)
        activityTake.append(maxActivity)
        top3Activity[maxActivity] = maxValue
        index += 1
      
      print(activityTake)
      print(top3Activity)
      print("")

      with open('./Data/MAXInferenceHomeB.csv', mode='w') as infereceA:
        infereceAWriter = csv.writer(infereceA, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      

        infereceAWriter.writerow(['A0', 'A1', 'A2'])
        infereceAWriter.writerow([top3Activity[activityTake[0]], top3Activity[activityTake[1]], top3Activity[activityTake[2]]])

      distribution_B = pd.read_csv('./Data/MAXInferenceHomeB.csv')

      return html.Div([
          html.H2("Activity"),
          html.H4(activityName_B)

      ]), html.Div([
            dcc.Graph(
            id='LastActivityDistribution',
                    figure={
                        'data': [
                            {'x': str(activityTake[0]), 'y': distribution_B.A0,
                                'type': 'bar', 'name': str(activityTake[0])},
                            {'x': str(activityTake[1]), 'y': distribution_B.A1,
                                'type': 'bar', 'name': str(activityTake[1])},
                            {'x': str(activityTake[2]), 'y': distribution_B.A2,
                                'type': 'bar', 'name': str(activityTake[2])},],
                        'layout': {
                    'title': 'Last Activity Distribution'
                        }
                    }
                ),

      ]) 



if __name__ == '__main__':
    app.run_server(debug=True)



