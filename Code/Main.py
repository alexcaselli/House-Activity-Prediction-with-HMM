from bayespy.nodes import CategoricalMarkovChain, Categorical, Mixture
import numpy as np
from Preprocessing import launchPreProcessing
from ComputeMatrix import computeTransitionMatrix, computeOsservationMatrix

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

firstOrderMC = CategoricalMarkovChain(initialPro, transictionMatrix, states=100)
observedProcess = Mixture(firstOrderMC, Categorical, osservationMatrix)


