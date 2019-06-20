from bayespy.nodes import CategoricalMarkovChain, Categorical, Mixture
import numpy as np
from Preprocessing import launchPreProcessing
from ComputeMatrix import computeTransitionMatrix, computeOsservationMatrix
from ModelRating import getCorrectActivitySequence, getAction
from bayespy.inference import VB
import bayespy.plot as bpplt
from hmmlearn import hmm
import math

#launchPreProcessing()

home = 'A'
transictionMatrix, initialPro = computeTransitionMatrix('A')
osservationMatrix = computeOsservationMatrix('A')

actionObserved = getAction("A", 'test')
correctActivity = getCorrectActivitySequence("A", 'test')
'''
home = 'B'
transictionMatrix, initialPro = computeTransitionMatrix('B')
osservationMatrix = computeOsservationMatrix('B')

actionObserved = getAction("B", 'test')
correctActivity = getCorrectActivitySequence("B", 'test')'''

# print(type(initialPro))
# print(initialPro)
# print("")
# print(type(transictionMatrix))
# print(transictionMatrix)
# print("")
# print(type(osservationMatrix))
# print(osservationMatrix)
# print("")

if (home == 'A'):
   model = hmm.MultinomialHMM(n_components=9)
   model.startprob_ = np.array(initialPro[0])
   model.transmat_ = np.array([transictionMatrix[0],
                              transictionMatrix[1],
                              transictionMatrix[2],
                              transictionMatrix[3],
                              transictionMatrix[4],
                              transictionMatrix[5],
                              transictionMatrix[6],
                              transictionMatrix[7],
                              transictionMatrix[8]])
         
   model.emissionprob_ = np.array([osservationMatrix[0],
                                 osservationMatrix[1],
                                 osservationMatrix[2],
                                 osservationMatrix[3],
                                 osservationMatrix[4],
                                 osservationMatrix[5],
                                 osservationMatrix[6],
                                 osservationMatrix[7],
                                 osservationMatrix[8]])
else:
      model = hmm.MultinomialHMM(n_components=10)
      model.startprob_ = np.array(initialPro[0])
      model.transmat_ = np.array([transictionMatrix[0],
                                 transictionMatrix[1],
                                 transictionMatrix[2],
                                 transictionMatrix[3],
                                 transictionMatrix[4],
                                 transictionMatrix[5],
                                 transictionMatrix[6],
                                 transictionMatrix[7],
                                 transictionMatrix[8],
                                 transictionMatrix[9]])
            
      model.emissionprob_ = np.array([osservationMatrix[0],
                                    osservationMatrix[1],
                                    osservationMatrix[2],
                                    osservationMatrix[3],
                                    osservationMatrix[4],
                                    osservationMatrix[5],
                                    osservationMatrix[6],
                                    osservationMatrix[7],
                                    osservationMatrix[8],
                                    osservationMatrix[9]])

# print(model.startprob_)
# print(model.transmat_)
# print(model.emissionprob_)

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

like = math.exp(model.score(np.array([[0]]))) #probabilità di avere oservations[2] per 3 volte di seguito
posteriors = model.predict(actionObserved.T)
print("ACTIVITY FROM OBSERVATION VALUE: ", posteriors)

cont = 0
for activity in range(0, len(correctActivity[0])):
   if posteriors[activity] != correctActivity[0][activity]:
      # print(activity)
      # print(posteriors[activity])
      # print(correctActivity[0][activity])
      cont += 1
      # print("")

print("WRONG INFERENCE: " + str(cont) + ' ON: ' + str(len(correctActivity[0])) + ' ACTIVITIES')

# [0: 'Breakfast', 1: 'Grooming', 2: 'Leaving', 3: 'Lunch', 4: 'Showering',
#  5: 'Sleeping', 6: 'Snack', 7: 'Spare_Time/TV', 8: 'Toileting']

# ['0: BasinPIRBathroom', 1: 'BedPressureBedroom', 2: 'CabinetMagneticBathroom', 
#  3: 'CooktopPIRKitchen', 4: 'CupboardMagneticKitchen', 5: 'FridgeMagneticKitchen', 
#  6: 'MaindoorMagneticEntrance', 7: 'MicrowaveElectricKitchen', 8: 'SeatPressureLiving', 
#  9: 'ShowerPIRBathroom', 10: 'ToasterElectricKitchen', 11: 'ToiletFlushBathroom']
'''
#hmmlearn
import numpy as np
from hmmlearn import hmm
states = ('Rainy', 'Sunny')
 
observations = ('walk', 'shop', 'clean')
 
start_probability = {'Rainy': 0.6, 'Sunny': 0.4}
 
transition_probability = {
   'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},
   'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6},
   }
 
emission_probability = {
   'Rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
   'Sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
   }

from hmmlearn import hmm
import numpy as np
import math

model = hmm.MultinomialHMM(n_components=2)
model.startprob_ = np.array([0.6, 0.4])
model.transmat_ = np.array([[0.7, 0.3],
                            [0.4, 0.6]])
model.emissionprob_ = np.array([[0.1, 0.4, 0.5],
                                [0.6, 0.3, 0.1]])

#problema 1, likelihood di avere una sequenza O (np.array([[oss1, oss2, oss3]]))
#usiamo math.exp perchè altrimenti sarebbe un logaritmo
like = math.exp(model.score(np.array([[2,2,2]]))) #probabilità di avere oservations[2] per 3 volte di seguito
print(like)

#problema 2, viterbi
logprob, seq = model.decode(np.array([[1,2,0]]).transpose())
print(math.exp(logprob))
print(seq)
'''
#prova con esercizio visto in classe
model = hmm.MultinomialHMM(n_components=2)
model.startprob_ = np.array([0.5, 0.5])
model.transmat_ = np.array([[0.7, 0.3],
                            [0.3, 0.7]])
model.emissionprob_ = np.array([[0.9, 0.1],
                                [0.2, 0.8]])

#problema 1, likelihood di avere una sequenza O (np.array([[oss1, oss2, oss3]]))
#usiamo math.exp perchè altrimenti sarebbe un logaritmo
# like = math.exp(model.score(np.array([[0]]))) #probabilità di avere oservations[2] per 3 volte di seguito
# print(like)

#non so
posteriors = model.predict_proba(np.array([[0, 0, 1, 0]]).T)
print(posteriors)
print("")
# viterbi = model.predict_proba(np.array([[1, 0, 1]]).T)
# print(viterbi)

#problema 2, viterbi
# logprob, seq = model.decode(np.array([[0,1,1]]).transpose())
# print(math.exp(logprob))
# print(seq)
'''


import random
from yahmm import *

model = Model(name='HouseModel')
breakfast = State(DiscreteDistribution( {'SeatPressureLiving': 0.1, 'CupboardMagneticKitchen': 0.4, 'FridgeMagneticKitchen': 0.4, 'CooktopPIRKitchen': 0.1 }))
spare_time = State(DiscreteDistribution( {'SeatPressureLiving': 0.7, 'CupboardMagneticKitchen': 0.1, 'FridgeMagneticKitchen': 0.1, 'CooktopPIRKitchen': 0.1 }))

model.add_transition(model.start, breakfast, 0.5)
model.add_transition(model.start, spare_time, 0.5)

model.add_transition(breakfast, breakfast, 0.65)
model.add_transition(breakfast, spare_time, 0.25)
model.add_transition(spare_time, breakfast, 0.15)
model.add_transition(spare_time, spare_time, 0.75)


model.add_transition(breakfast, model.end, 0.1)
model.add_transition(spare_time, model.end, 0.1)

Model.draw(model)
model.bake()

print(model.sample)'''
'''
print(distribution)
print(state)



firstOrderMC = CategoricalMarkovChain(initialPro, transictionMatrix, states = 391)
observedProcess = Mixture(firstOrderMC, Categorical, osservationMatrix)

correctActivity = getCorrectActivitySequence("A")
# print(len(correctActivity[0]))

osservation = getAction("A")
# print(len(osservation[0]))

observedProcess.observe(osservation)

inferenceProcess = VB(observedProcess, firstOrderMC)

inferenceProcess.update()
import bayespy.plot as bpplt
bpplt.plot(firstOrderMC)
bpplt.plot(1-correctActivity, color='r', marker='x')
inferenceProcess.plot_iteration_by_nodes()
'''




