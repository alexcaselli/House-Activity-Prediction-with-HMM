import csv
import numpy as np
from math import floor
from hmmlearn import hmm
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import matplotlib.pyplot as plotly
import plotly.io as pio



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
        print("{:<33}{:>4}".format("LIM VALUE FROM CORRECT ACTIVITY: ", len(activity)- 1 - lim+1))
        print("")
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
        print("{:<33}{:>4}".format("LIM VALUE FROM CORRECT ACTION: ", len(actionSequence)- 1 - lim+1))
        return np.array([actionSequence[lim+1:len(actionSequence)-1]])
    else:
        return np.array([actionSequence])


    # ['0: BasinPIRBathroom', 1: 'BedPressureBedroom', 2: 'CabinetMagneticBathroom', 
#  3: 'CooktopPIRKitchen', 4: 'CupboardMagneticKitchen', 5: 'FridgeMagneticKitchen', 
#  6: 'MaindoorMagneticEntrance', 7: 'MicrowaveElectricKitchen', 8: 'SeatPressureLiving', 
#  9: 'ShowerPIRBathroom', 10: 'ToasterElectricKitchen', 11: 'ToiletFlushBathroom']

def printInformation(initialPro, transictionMatrix, observationsMatrix, actionObserved, correctActivity):

    print("")
    print("######################################")
    print("#", end = " ")
    print("{:<28}{:<7}".format("TRANSICTION MATRIX SIZE: ", str(transictionMatrix.shape)), end = "")
    print("#")
    print("#", end = " ")
    print("{:<28}{:<7}".format("INITIAL PROBABILITIES SIZE: ", str(initialPro.shape)), end = "")
    print("#")
    print("#", end = " ")
    print("{:<28}{:<7}".format("OSSERVATION MATRIX SIZE: ", str(observationsMatrix.shape)), end = "")
    print("#")
    print("######################################")
    print("")

    print("INITIAL PROBABILITY")
    print(type(initialPro))
    print(initialPro)
    print("")

    print("TRANSICTION MATRIX")
    print(type(transictionMatrix))
    print(transictionMatrix)
    print("")

    print("OBSERVATION MATRIX")
    print(type(observationsMatrix))
    print(observationsMatrix)
    print("")

    print("ACTION OBSERVED")
    print(type(actionObserved))
    print(actionObserved)
    print("")

    print("CORRECT ACTIVITIY")
    print(type(correctActivity))
    print(correctActivity)
    print("")

def modelRating(model, actionObserved, correctActivity, matrixSize, targetActivityName):

    posteriors = model.predict_proba(actionObserved.T)
    # print("ACTIVITY FROM OBSERVATION VALUE: ", posteriors)
    postery = list()

    confusionMatrix = np.zeros((matrixSize, matrixSize))

    cont = 0
    for activity in range(0, len(correctActivity[0])):
        decision = np.where(posteriors[activity] == np.amax(posteriors[activity]))
        if decision[0] != correctActivity[0][activity]:
            # print(activity)
            # print(posteriors[activity])
            # print(correctActivity[0][activity])
            cont += 1
            # print("")
        postery.append(decision[0])
        confusionMatrix[correctActivity[0][activity]][decision[0]] += 1

    # plotConfusionMatrix(correctActivity[0], postery, targetActivityName, False, "Confusion Matrix")

    print("CONFUSION MATRIX")
    print(confusionMatrix)
    print("WRONG INFERENCE: " + str(cont) + ' ON: ' + str(len(correctActivity[0])) + ' ACTIVITIES')


    print(classification_report(correctActivity[0], postery, target_names=targetActivityName))
    print("")
    print("ACCURACY SCORE:", end = " ")
    print(accuracy_score(correctActivity[0], postery))


# [0: 'Breakfast', 1: 'Grooming', 2: 'Leaving', 3: 'Lunch', 4: 'Showering',
#  5: 'Sleeping', 6: 'Snack', 7: 'Spare_Time/TV', 8: 'Toileting']

# ['0: BasinPIRBathroom', 1: 'BedPressureBedroom', 2: 'CabinetMagneticBathroom', 
#  3: 'CooktopPIRKitchen', 4: 'CupboardMagneticKitchen', 5: 'FridgeMagneticKitchen', 
#  6: 'MaindoorMagneticEntrance', 7: 'MicrowaveElectricKitchen', 8: 'SeatPressureLiving', 
#  9: 'ShowerPIRBathroom', 10: 'ToasterElectricKitchen', 11: 'ToiletFlushBathroom'] plt.cm.Blues

def plotConfusionMatrix(y_true, y_pred, classes, normalize, title, cmap= plotly.cm.get_cmap("Blues")):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    # classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plotly.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap= cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plotly.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()

    plotly.show(ax)
    
