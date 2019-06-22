from hmmlearn import hmm
import numpy as np

def buildModel(initialPro, transictionMatrix, osservationMatrix):

    transMat = np.array([transictionMatrix[0]])
    emissionMat = np.array([osservationMatrix[0]])

    for i in range(1, len(transictionMatrix)):
        transMat = np.append(transMat, [transictionMatrix[i]], axis = 0)
        emissionMat = np.append(emissionMat, [osservationMatrix[i]], axis = 0)
    
    model = hmm.MultinomialHMM(n_components=len(transictionMatrix))
    model.startprob_ = np.array(initialPro[0])
    model.transmat_ = transMat
    model.emissionprob_ = emissionMat

    return model

