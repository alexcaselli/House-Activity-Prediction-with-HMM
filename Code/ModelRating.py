import csv
import numpy as np
from math import floor


def getCorrectActivitySequence(home, stage):

    activity = list()

    with open("./Dataset/datasetCSV/labeled"+home+".csv", "r") as correctActivity:
        reader = csv.reader(correctActivity, delimiter = ';', quoting=csv.QUOTE_ALL)
        next(reader)
        #dictionary for indexing in T
        activ_dict = {}
        index = 0
        if (home == 'A'):
            sorted_act = ['Breakfast', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']
        else:
            sorted_act = ['Breakfast', 'Dinner', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']

        for act in sorted_act:
            activ_dict[act] = index
            index += 1

        for line in reader:
            act_name = line[1]
            activity.append(activ_dict[act_name])
        
    # print(actionSequence)
    if (stage == 'test'):
        #test samples
        lim = floor(len(activity)*0.7)
        print("LIM VALUE FROM CORRECT ACTIVITY: ", len(activity)- 1 - lim+1)
        return np.array([activity[lim+1:len(activity)-1]])
    else:
        return np.array([activity])


# [0: 'Breakfast', 1: 'Grooming', 2: 'Leaving', 3: 'Lunch', 4: 'Showering',
#  5: 'Sleeping', 6: 'Snack', 7: 'Spare_Time/TV', 8: 'Toileting']

def getAction(home, stage):

    actionSequence = list()

    with open("./Dataset/datasetCSV/labeled"+home+".csv", "r") as action:
        reader = csv.reader(action, delimiter = ';', quoting=csv.QUOTE_ALL)
        next(reader)

        if (home == 'A'):
            sorted_oss = ['BasinPIRBathroom', 'BedPressureBedroom', 'CabinetMagneticBathroom', 'CooktopPIRKitchen', 'CupboardMagneticKitchen', 'FridgeMagneticKitchen', 'MaindoorMagneticEntrance',
                'MicrowaveElectricKitchen', 'SeatPressureLiving', 'ShowerPIRBathroom', 'ToasterElectricKitchen', 'ToiletFlushBathroom']
        else:
            sorted_oss = ['BasinPIRBathroom', 'BedPressureBedroom', 'CupboardMagneticKitchen', 'DoorPIRBedroom', 'DoorPIRKitchen', 'DoorPIRLiving', 'FridgeMagneticKitchen',
             'MaindoorMagneticEntrance', 'MicrowaveElectricKitchen', 'SeatPressureLiving', 'ShowerPIRBathroom', 'ToiletFlushBathroom']

        #dictionary for indexing Activity in O
        oss_dict = {}
        index = 0
        for oss_name in sorted_oss:
            oss_dict[oss_name] = index
            index+=1
            
        for line in reader:
            action = ''
            action += line[2]+line[3]+line[4]
            actionSequence.append(oss_dict[action])


    # print(actionSequence)
    if stage == 'test':
        #test samples
        lim = floor(len(actionSequence)*0.7)
        print("LIM VALUE FROM CORRECT ACTION: ", len(actionSequence)- 1 - lim+1)
        return np.array([actionSequence[lim+1:len(actionSequence)-1]])
    else:
        return np.array([actionSequence])


    # ['0: BasinPIRBathroom', 1: 'BedPressureBedroom', 2: 'CabinetMagneticBathroom', 
#  3: 'CooktopPIRKitchen', 4: 'CupboardMagneticKitchen', 5: 'FridgeMagneticKitchen', 
#  6: 'MaindoorMagneticEntrance', 7: 'MicrowaveElectricKitchen', 8: 'SeatPressureLiving', 
#  9: 'ShowerPIRBathroom', 10: 'ToasterElectricKitchen', 11: 'ToiletFlushBathroom']
