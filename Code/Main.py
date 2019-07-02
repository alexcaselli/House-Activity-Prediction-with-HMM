# OUR CLASS
from Preprocessing import launchPreProcessing
from ComputeMatrix import computeTransitionMatrix, computeOsservationMatrix
from ModelRating import getCorrectActivitySequence, getAction, printInformation, modelRating
from BuildModel import buildModel

import warnings
import pickle
import math

# DISABLE WARNINGS BY SKLEARN.METRICS
# warnings.filterwarnings('ignore') 

################################ DONE PREPROCESSING ################################
#launchPreProcessing()



################################ GET PARAMETER FOR MODEL ################################
transictionMatrixA, initialProA = computeTransitionMatrix('A', True)
osservationMatrixA = computeOsservationMatrix('A', True)
actionObservedA = getAction("A", 'test')
correctActivityA = getCorrectActivitySequence("A", 'test')

transictionMatrixB, initialProB = computeTransitionMatrix('B', True)
osservationMatrixB = computeOsservationMatrix('B', True)
actionObservedB = getAction("B", 'test')
correctActivityB = getCorrectActivitySequence("B", 'test')



################################ SET TARGET ACTIVITY ################################
targetActivityNameA = ['Breakfast', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']
targetActivityNameB = ['Breakfast', 'Dinner', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']



################################ SHOW INFORMATION ################################
# printInformation(initialProA, transictionMatrixA, osservationMatrixA, actionObservedA, correctActivityA)
# printInformation(initialProB, transictionMatrixB, osservationMatrixB, actionObservedB, correctActivityB)



################################ MODEL BUILDING ################################
modelA = buildModel(initialProA, transictionMatrixA, osservationMatrixA)
modelB = buildModel(initialProB, transictionMatrixB, osservationMatrixB)



################################ MODEL RATING ################################
print("---------------MODEL A RATING---------------")
modelRating(modelA, actionObservedA, correctActivityA, len(transictionMatrixA), targetActivityNameA)
print("--------------------------------------------")
print("")
print("---------------MODEL B RATING---------------")
modelRating(modelB, actionObservedB, correctActivityB, len(transictionMatrixB), targetActivityNameB)
print("--------------------------------------------")
print(" ")

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
print("-.-.-.-.-.-.-.-FINAL MODEL-.-.-.-.-.-.-.-")
################################ GET FINAL MODEL ################################
transictionMatrixA, initialProA = computeTransitionMatrix('A', False)
osservationMatrixA = computeOsservationMatrix('A', False)
actionObservedA = getAction("A", 'no_test')
correctActivityA = getCorrectActivitySequence("A", 'no_test')

transictionMatrixB, initialProB = computeTransitionMatrix('B', False)
osservationMatrixB = computeOsservationMatrix('B', False)
actionObservedB = getAction("B", 'no_test')
correctActivityB = getCorrectActivitySequence("B", 'no_test')



################################ SET TARGET ACTIVITY ################################
targetActivityNameA = ['Breakfast', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']
targetActivityNameB = ['Breakfast', 'Dinner', 'Grooming', 'Leaving', 'Lunch', 'Showering', 'Sleeping', 'Snack', 'Spare_Time/TV', 'Toileting']


################################ SHOW INFORMATION ################################
# printInformation(initialProA, transictionMatrixA, osservationMatrixA, actionObservedA, correctActivityA)
# printInformation(initialProB, transictionMatrixB, osservationMatrixB, actionObservedB, correctActivityB)



################################ MODEL BUILDING ################################
modelA = buildModel(initialProA, transictionMatrixA, osservationMatrixA)
modelB = buildModel(initialProB, transictionMatrixB, osservationMatrixB)



################################ MODEL RATING ################################
print("-.-.-.-.-.-.-.-MODEL A RATING-.-.-.-.-.-.-.-")
modelRating(modelA, actionObservedA, correctActivityA, len(transictionMatrixA), targetActivityNameA)
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print("")
print("-.-.-.-.-.-.-.-MODEL B RATING-.-.-.-.-.-.-.-")
modelRating(modelB, actionObservedB, correctActivityB, len(transictionMatrixB), targetActivityNameB)
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print(" ")


################################ SAVING MODEL ################################
with open("./Model/HouseA.pkl", "wb") as fileA: 
   pickle.dump(modelA, fileA)
with open("./Model/HouseB.pkl", "wb") as fileB: 
   pickle.dump(modelB, fileB)



################################ TEST LOAD MODEL ################################
with open("./Model/HouseA.pkl", "rb") as fileA: 
   modelA = pickle.load(fileA)
with open("./Model/HouseB.pkl", "rb") as fileB: 
   modelB = pickle.load(fileB)



################################ LOAD MODEL RATING ################################
print("")
print("=.=.=.=.=.=.=.=LOAD MODEL RATING=.=.=.=.=.=.=.=")
print("")
print("=.=.=.=.=.=.=.=MODEL A RATING=.=.=.=.=.=.=.=")
modelRating(modelA, actionObservedA, correctActivityA, len(transictionMatrixA), targetActivityNameA)
print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=")
print("")
print("=.=.=.=.=.=.=.=MODEL B RATING=.=.=.=.=.=.=.=")
modelRating(modelB, actionObservedB, correctActivityB, len(transictionMatrixB), targetActivityNameB)
print("=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.= ")
print(" ")

