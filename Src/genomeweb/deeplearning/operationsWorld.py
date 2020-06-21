# Este arquivo contém os algoritmos para treinamentos das Redes Neurais

try:
    from . import operationsPermutation
    from . import neuralNetworks
except:
    import operationsPermutation
    import neuralNetworks
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
from datetime import datetime


def getScoreForAllSigmas(permutation, sigmas, model):
    return [model.predict(np.array([operationsPermutation.join(permutation, sigma)]))[0][0] for sigma in sigmas]


def getRouteScore(permutation, dqn, protectBreakpoints):
    routeScore = []
    moves = 0
    while (moves < dqn.movesLimit) and (operationsPermutation.isIdentity(permutation) == False):
        moves += 1
        if protectBreakpoints:
            sigmas = operationsPermutation.getSigmasProtectionBreakpoint(permutation, operationsPermutation.getAllReversals)
        else:
            sigmas = operationsPermutation.getAllSigmas(permutation, operationsPermutation.getAllReversals)
        scores = getScoreForAllSigmas(permutation, sigmas, dqn.model)
        biggerScore =  max(scores)
        intention = sigmas[scores.index(max(scores))]
        nextPermutation = operationsPermutation.nextByPermutationMarkovDecisionProcess(sigmas, intention, dqn.temperature)
        routeScore.append((permutation, nextPermutation, biggerScore))
        permutation = nextPermutation
    return routeScore, permutation


def trainModelByBellmanEquation(model, gamma, routeScore):
    if routeScore != []:
        inputs = [operationsPermutation.join(score[0], score[1]) for score in routeScore]
        targets = [1 if(i == len(routeScore) - 1) else (float)(gamma * routeScore[i+1][2]) for i in range(0, len(routeScore))]
        model.fit(np.array(inputs), np.array(targets),  verbose = 0)
    return model


def defaultTrain(dqn, epochs, protectBreakpoints = False):
    for epoch in range(epochs):
        t1 = datetime.today()
        print("Processing Training: {}%".format(100 * epoch//epochs), end="")
        startPermutation = operationsPermutation.randomState(dqn.permutation_size)
        routeScore, lastPermutation = getRouteScore(startPermutation, dqn, protectBreakpoints)
        if operationsPermutation.isIdentity(lastPermutation) == True:
            trainModelByBellmanEquation(dqn.model, dqn.gamma, routeScore)
        t2 = datetime.today()
        print(" - Tempo Restante: {}s".format((t2-t1) * (epochs - epoch)))
        

def trainWithPenalty(dqn, epochs, protectBreakpoints = False):
    for epoch in range(epochs):
        t1 = datetime.today()
        print("Processing Training: {}%".format(100 * epoch//epochs), end="")
        startPermutation = operationsPermutation.randomState(dqn.permutation_size)
        routeScore, lastPermutation = getRouteScore(startPermutation, dqn, protectBreakpoints)
        if operationsPermutation.isIdentity(lastPermutation) == True:
            trainModelByBellmanEquation(dqn.model, dqn.gamma, routeScore)
        t2 = datetime.today()
        print(" - Tempo Restante: {}s".format((t2-t1) * (epochs - epoch)))


def trainWithBreakPoints(dqn, epochs):
        inputs = []
        targets = []
        for epoch in range(epochs):
            t1 = datetime.today()
            print("Breakpoint Training: {}%".format(100 * epoch//epochs), end="")
            startPermutation = operationsPermutation.randomState(dqn.permutation_size)
            numBkpPermutation = operationsPermutation.getNumberBreakPoints(startPermutation)
            sigmas = operationsPermutation.getAllSigmas(startPermutation, operationsPermutation.getAllReversals)
            score = None
            for sigma in sigmas:
                numBkpSigma = operationsPermutation.getNumberBreakPoints(sigma)
                difference = numBkpPermutation - numBkpSigma
                if difference == 0:
                    score = 0
                elif difference >= 1:
                    score = 1
                else:
                    score = -1
                inputs.append(operationsPermutation.join(startPermutation, sigma))
                targets.append(score)
            t2 = datetime.today()
            print(" - Tempo Restante: {}s".format((t2-t1) * (epochs - epoch)))
        dqn.model.fit(np.array(inputs), np.array(targets))


def goIdentity(permutation, dqn):
    start = list(permutation)
    routeScore = []
    moves = 0
    while (moves < dqn.movesLimit) and (operationsPermutation.isIdentity(permutation) == False):
        moves += 1
        sigmas = operationsPermutation.getAllSigmas(permutation, operationsPermutation.getAllReversals)
        scores = getScoreForAllSigmas(permutation, sigmas, dqn.model)
        biggerScore =  max(scores)
        intention = sigmas[scores.index(max(scores))]
        nextPermutation = intention
        routeScore.append((permutation, nextPermutation, scores[sigmas.index(nextPermutation)]))
        permutation = nextPermutation
    if moves < dqn.movesLimit:
        print("------------------------")
        print("A rede convergiu!")
        print("------------------------")
        print("Início: ", start)
        for avanco in routeScore:
            print("-->", avanco[1])
        print("------------------------")
        print("Total de reversões:", moves)
        print("------------------------")
    else:
        print("------------------------")
        print("A Rede ainda não convergiu!")
        print("------------------------")