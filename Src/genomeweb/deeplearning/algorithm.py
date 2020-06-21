import operationsPermutation, neuralNetworks, operationsWorld
import numpy as np

deepQNetwork = neuralNetworks.DqnKeras(4)
operationsWorld.trainWithBreakPoints(deepQNetwork, 50000)
deepQNetwork.saveNetwork("redes/network{}s.h5".format(1))

operationsWorld.goIdentity(operationsPermutation.randomState(deepQNetwork.permutation_size), deepQNetwork)