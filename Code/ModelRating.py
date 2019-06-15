import csv
import numpy as np


def getCorrectActivitySequence(home):

    activity = list()

    with open("./Dataset/datasetCSV/labeled"+home+".csv", "r") as correctActivity:
        reader = csv.reader(correctActivity, delimiter = ';', quoting=csv.QUOTE_ALL)
        next(reader)

        for line in reader:
            if line[1] == "Breakfast":
                activity.append(0)
            elif line[1] == "Grooming":
                activity.append(1)
            elif line[1] == "Leaving":
                activity.append(2)
            elif line[1] == "Lunch":
                activity.append(3)
            elif line[1] == "Showering":
                activity.append(4)
            elif line[1] == "Sleeping":
                activity.append(5)
            elif line[1] == "Snack":
                activity.append(6)
            elif line[1] == "Spare_Time/TV":
                activity.append(7)
            elif line[1] == "Toileting":
                activity.append(8)
            else:
                print("this is a problem...")
                print(line)

        # print(activity)

    return np.array([activity])


# [0: 'Breakfast', 1: 'Grooming', 2: 'Leaving', 3: 'Lunch', 4: 'Showering',
#  5: 'Sleeping', 6: 'Snack', 7: 'Spare_Time/TV', 8: 'Toileting']

def getAction(home):

    actionSequence = list()

    with open("./Dataset/datasetCSV/labeled"+home+".csv", "r") as action:
        reader = csv.reader(action, delimiter = ';', quoting=csv.QUOTE_ALL)
        next(reader)

        for line in reader:
            action = ""
            action += line[2]+line[3]+line[4]
            if action == "BasinPIRBathroom":
                actionSequence.append(0)
            elif action == "BedPressureBedroom":
                actionSequence.append(1)
            elif action == "CabinetMagneticBathroom":
                actionSequence.append(2)
            elif action == "CooktopPIRKitchen":
                actionSequence.append(3)
            elif action == "CupboardMagneticKitchen":
                actionSequence.append(4)
            elif action == "FridgeMagneticKitchen":
                actionSequence.append(5)
            elif action == "MaindoorMagneticEntrance":
                actionSequence.append(6)
            elif action == "MicrowaveElectricKitchen":
                actionSequence.append(7)
            elif action == "SeatPressureLiving":
                actionSequence.append(8)
            elif action == "ShowerPIRBathroom":
                actionSequence.append(9)
            elif action == "ToasterElectricKitchen":
                actionSequence.append(10)
            elif action == "ToiletFlushBathroom":
                actionSequence.append(11)
            else:
                print("this is a problem...")
                print(line)

    # print(actionSequence)

    return np.array([actionSequence])


    # ['0: BasinPIRBathroom', 1: 'BedPressureBedroom', 2: 'CabinetMagneticBathroom', 
#  3: 'CooktopPIRKitchen', 4: 'CupboardMagneticKitchen', 5: 'FridgeMagneticKitchen', 
#  6: 'MaindoorMagneticEntrance', 7: 'MicrowaveElectricKitchen', 8: 'SeatPressureLiving', 
#  9: 'ShowerPIRBathroom', 10: 'ToasterElectricKitchen', 11: 'ToiletFlushBathroom']