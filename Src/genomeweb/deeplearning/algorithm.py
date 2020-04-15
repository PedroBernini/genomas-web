import operationsPermutation, neuralNetworks, learn
import numpy as np

deepQNetwork = neuralNetworks.DqnKeras(3)
valueExit = deepQNetwork.model.predict(np.array([[1,2,3,4,5,6]]))[0]
print(valueExit[0])