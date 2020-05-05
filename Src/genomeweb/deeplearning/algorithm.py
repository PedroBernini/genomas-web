import operationsPermutation, neuralNetworks, operationsWorld
import numpy as np

deepQNetwork = neuralNetworks.DqnKeras(3)
operationsWorld.worldTrain(deepQNetwork, 10)
operationsWorld.goIdentity(operationsPermutation.randomState(3), deepQNetwork)