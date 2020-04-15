# Este arquivo contém os algoritmos para treinamentos das Redes Neurais

import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import operationsPermutation
import neuralNetworks

def getScoreForAllSigmas(permutation, sigmas, model):
    return [model.predict(np.array([operationsPermutation.join(permutation, sigma)]))[0][0] for sigma in sigmas]

def getRouteScore(permutation, dqn):
    routeScore = []
    moves = 0
    while (moves < dqn.movesLimit) and (operationsPermutation.isIdentity(permutation) == False):
        # MELHORAR LOGICA LIMIT MOVES
        moves += 1

        # MELHORAR LOGICA GET MAIOR SCORE
        sigmas = operationsPermutation.getAllSigmas(permutation)
        scores = getScoreForAllSigmas(permutation, sigmas, dqn.model)
        biggerScore = max(scores) # Rever a necessidade dele
        intention = sigmas[scores.index(max(scores))]
        nextPermutation = operationsPermutation.nextByPermutationMarkovDecisionProcess(sigmas, intention, dqn.temperature)

        routeScore.append((permutation, nextPermutation, biggerScore)) # Rever a necessidade do bigger
        if len(routeScore) > dqn.memoryCapacity: # Rever a necessidade dele
            del routeScore[0] # Rever a necessidade dele
        permutation = nextPermutation
        print(permutation)
    
    return routeScore, permutation

def trainModelByBellmanEquation(model, gamma, routeScore):
    if routeScore != []:
        inputs = [operationsPermutation.join(score[0], score[1]) for score in routeScore]
        targets = [1 if(i == len(routeScore) - 1) else (float)(gamma * routeScore[i+1][2]) for i in range(0, len(routeScore))]
        model.fit(np.array(inputs), np.array(targets))
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
        sigmas = operationsPermutation.getAllSigmas(pi)
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
    
dqn = neuralNetworks.DqnKeras(3)
worldTrain(dqn, 1000)
goIdentity([3,2,1], dqn)
    
    
    
    
    
    
    
    
    

'''
if not oneFit:
    
else:
    fits = []
    for epoca in range(length):
        print("Epoca:", epoca + 1, "/", length)
        pi = self.randomState()
        tableScore = []
        moves = 0
        while (moves < self.movesLimit) and (self.isIdentity(pi) == False):
            moves += 1
            results = []
            choices = []
            sigmas = self.getSigmas(pi)
            for sigma in sigmas:
                state = self.join(pi, sigma)
                valueExit = self.model.predict(np.array([state]))[0]
                results.append(valueExit[0])
                choices.append(sigma)
            biggerScore = max(results)
            intention = sigmas[results.index(max(results))]
            nextState = self.markovDecision(choices, intention, self.temperature)
            tableScore.append((pi, nextState, biggerScore))
            if len(tableScore) > self.memoryCapacity:
                del tableScore[0]
            pi = nextState
        if (self.isIdentity(pi) == True):
            inputs = []
            targets = []
            score = 1
            tableScore.reverse()
            for i in range(0, len(tableScore)):
                state = self.join(tableScore[i][0], tableScore[i][1])
                inputs.append(state)
                if i == 0:
                    score = 1
                else:
                    score = score * self.gamma
                targets.append(score)
            fits.append((inputs, targets))
            print("FIT SUCESSO =)")
        else:
            print("FIT FRACASSO =(")
            
    print("\nTotal de Fits Sucedidos:", len(fits))
    print("Treinando...")
    for fit in fits: 
        try:
            self.model.fit(np.array(fit[0]), np.array(fit[1]))
        except:
            pass'''