from bayespy.nodes import CategoricalMarkovChain, Categorical, Mixture
import numpy as np
from Preprocessing import launchPreProcessing
from ComputeMatrix import computeTransitionMatrix, computeOsservationMatrix
from ModelRating import getCorrectActivitySequence, getAction
from bayespy.inference import VB
import bayespy.plot as bpplt

launchPreProcessing()

transictionMatrix, initialPro = computeTransitionMatrix('A')
osservationMatrix = computeOsservationMatrix('A')

# print(transictionMatrix)

print("")
print("######################################")
print("#", end = " ")
print("{:<28}{:<7}".format("TRANSICTION MATRIX SIZE: ", str(transictionMatrix.shape)), end = "")
print("#")
print("#", end = " ")
print("{:<28}{:<7}".format("INITIAL PROBABILITIES SIZE: ", str(initialPro.shape)), end = "")
print("#")
print("#", end = " ")
print("{:<28}{:<7}".format("OSSERVATION MATRIX SIZE: ", str(osservationMatrix.shape)), end = "")
print("#")
print("######################################")
print("")


firstOrderMC = CategoricalMarkovChain(initialPro, transictionMatrix, states = 391)
observedProcess = Mixture(firstOrderMC, Categorical, osservationMatrix)

correctActivity = getCorrectActivitySequence("A")
# print(len(correctActivity[0]))

osservation = getAction("A")
# print(len(osservation[0]))

observedProcess.observe(osservation)

inferenceProcess = VB(observedProcess, firstOrderMC)

inferenceProcess.update()

inferenceProcess.plot_iteration_by_nodes()


# [0: 'Breakfast', 1: 'Grooming', 2: 'Leaving', 3: 'Lunch', 4: 'Showering',
#  5: 'Sleeping', 6: 'Snack', 7: 'Spare_Time/TV', 8: 'Toileting']

# ['0: BasinPIRBathroom', 1: 'BedPressureBedroom', 2: 'CabinetMagneticBathroom', 
#  3: 'CooktopPIRKitchen', 4: 'CupboardMagneticKitchen', 5: 'FridgeMagneticKitchen', 
#  6: 'MaindoorMagneticEntrance', 7: 'MicrowaveElectricKitchen', 8: 'SeatPressureLiving', 
#  9: 'ShowerPIRBathroom', 10: 'ToasterElectricKitchen', 11: 'ToiletFlushBathroom']


