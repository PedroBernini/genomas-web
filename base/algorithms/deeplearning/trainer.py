from base.algorithms.deeplearning import operationsPermutation, neuralNetworks, operationsWorld
from base import views

def createDqn(lengthPermutation, optimizerFunction='adam', lossFunction='mean_absolute_error'):
    return neuralNetworks.DqnKeras(lengthPermutation, optimizerFunction=optimizerFunction, lossFunction=lossFunction)

def trainNetwork(dqn, epochs):
    operationsWorld.trainWithBreakPoints(dqn, epochs)

def saveNetwork(dqn, nameNetwork):
    dqn.saveNetwork(views.PATH_NETWORKS + nameNetwork + '.h5')
