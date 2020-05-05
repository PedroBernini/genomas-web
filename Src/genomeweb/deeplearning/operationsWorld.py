# Este arquivo contém os algoritmos para treinamentos das Redes Neurais

import numpy as np
import operationsPermutation
import neuralNetworks
import keras
from keras.models import Sequential
from keras.layers import Dense
from datetime import datetime


def getScoreForAllSigmas(permutation, sigmas, model):
    return [model.predict(np.array([operationsPermutation.join(permutation, sigma)]))[0][0] for sigma in sigmas]


def getRouteScore(permutation, dqn):
    routeScore = []
    moves = 0
    while (moves < dqn.movesLimit) and (operationsPermutation.isIdentity(permutation) == False):
        moves += 1

        # MELHORAR LOGICA GET MAIOR SCORE
        sigmas = operationsPermutation.getAllSigmas(permutation, operationsPermutation.getAllReversals)
        scores = getScoreForAllSigmas(permutation, sigmas, dqn.model)
        biggerScore =  max(scores) # Rever a necessidade dele
        intention = sigmas[scores.index(max(scores))]

        nextPermutation = operationsPermutation.nextByPermutationMarkovDecisionProcess(sigmas, intention, dqn.temperature)
        # ARRUMAR ESTA PARTE QUE TA LIXO
        if nextPermutation
        routeScore.append((permutation, nextPermutation, scores[permutations.index(permutation)])) # Rever a necessidade do bigger
        permutation = nextPermutation
    
    return routeScore, permutation

def trainModelByBellmanEquation(model, gamma, routeScore):
    if routeScore != []:
        inputs = [operationsPermutation.join(score[0], score[1]) for score in routeScore]
        targets = [1 if(i == len(routeScore) - 1) else (float)(gamma * routeScore[i+1][2]) for i in range(0, len(routeScore))]
        model.fit(np.array(inputs), np.array(targets),  verbose = 1)
    return model

def worldTrain(dqn, epochs):
    for epoch in range(epochs):
        startPermutation = operationsPermutation.randomState(dqn.permutation_size)
        routeScore, lastPermutation = getRouteScore(startPermutation, dqn)
        if operationsPermutation.isIdentity(lastPermutation) == True:
            trainModelByBellmanEquation(dqn.model, dqn.gamma, routeScore)
        
def goIdentity(start, dqn): 
    pi = start
    tableScore = []
    qtdReversoes = 0
    movimentos = 0
    while (operationsPermutation.isIdentity(pi) == False and movimentos < 2*dqn.permutation_size):
        movimentos += 1
        qtdReversoes += 1
        results = []
        choices = []
        sigmas = operationsPermutation.getAllSigmas(pi, operationsPermutation.getAllReversals)
        for sigma in sigmas:
            state = operationsPermutation.join(pi, sigma)
            valueExit = dqn.model.predict(np.array([state]))[0]
            results.append(valueExit[0])
            choices.append(sigma)
        biggerScore = max(results)
        intention = sigmas[results.index(max(results))]
        nextState = intention
        tableScore.append((pi, nextState, biggerScore))
        pi = nextState
    if movimentos < 2*dqn.permutation_size:
        print("\nEstado inicial", start)
        print("Caminho Percorrido: ")
        for el in tableScore:
            print("-->", el[1], "\tScore:", '{:.4f}'.format(el[2]))
        print("Total de reversões:", qtdReversoes)
    else:
        print("Rede não convergiu!")