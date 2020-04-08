# Este arquivo contém os algoritmos para treinamentos das Redes Neurais

import keras
from keras.models import Sequential
from keras.layers import Dense
from . import operationsPermutation

def realisticTrain(model, length):
    for epoca in range(length):
        startPermutation = operationsPermutation.randomState(model.permutation_size)
        tableScore = []
        while (self.movesLimit > 0) and (operationsPermutation.isIdentity(startPermutation) == False):
            self.movesLimit -= 1
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
            for i in range(0, len(tableScore)):
                state = self.join(tableScore[i][0], tableScore[i][1])
                inputs.append(state)
                if i == len(tableScore) - 1:
                    score = 1
                else:
                    score = (float)(self.gamma * tableScore[i+1][2])
                targets.append(score)
            try:
                self.model.fit(np.array(inputs), np.array(targets))
            except:
                pass
            print("Chegou na Identidade =)")
        else:
            print("Falhou em chegar na Identidade =(")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
                pass