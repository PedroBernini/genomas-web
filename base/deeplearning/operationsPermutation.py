# Este arquivo contém todas as operações necessárias para as permutações

import numpy as np
import itertools
import random

def getAllBreakPoints(permutation):
    breakpoints = [(i + 1) for i in range(0, len(permutation) - 1) if (isAdjacent(permutation[i], permutation[i+1]) is False)]
    if(permutation[0] != 1):
        breakpoints.append(0)
    if(permutation[len(permutation) - 1] != len(permutation)):
        breakpoints.append(len(permutation))
    return breakpoints


def getAllReversals(n):
    return [(i, j) for i in range(0, n) for j in range(i + 1, n)]


def getAllPermutations(n):
    return [list(permutation) for permutation in itertools.permutations([i for i in range(1, n + 1)])]


def getAllSigmas(permutation, operation):
    return [applyReversal(permutation, rev[0], rev[1]) for rev in operation(len(permutation))]


def getAllScores(model):
    return [[(permutation, sigma, model.predict(np.array([join(permutation, sigma)]))[0][0]) for sigma in getAllSigmas(permutation, getAllReversals)] for permutation in getAllPermutations(3)]


def getSigmasProtectionBreakpoint(permutation, operation):
    return [applyReversal(permutation, rev[0], rev[1]) for rev in operation(len(permutation)) if rev[0] in getAllBreakPoints(permutation) and (rev[1] + 1) in getAllBreakPoints(permutation)]


def getNumberBreakPoints(permutation) :
    return len(getAllBreakPoints(permutation))


def getIdentity(n):
    return [i for i in range(1, n + 1)]


def isIdentity(permutation):
    return permutation == [i for i in range(1, len(permutation) + 1)]


def isAdjacent(x, y) :
    return abs(x - y) == 1


def join(permutation, sigma):
    return permutation + sigma


def randomState(n):
    identity = [i for i in range(1, n + 1)]
    np.random.shuffle(identity)
    return identity


def applyReversal(permutation, i, j):
    if(i > j):
        i, j = j, i
    strip = permutation[i:j+1]
    strip.reverse()
    return permutation[0:i] + strip + permutation[j+1:len(permutation)]


def nextByPermutationMarkovDecisionProcess(choices, intention, temperature):
    choices = list(choices)
    choices.remove(intention)
    if choices == []:
        return intention
    result = np.array([intention, random.choice(choices)])
    index = np.random.choice(a = [0, 1], size = 1, replace = True, p = [temperature, 1 - temperature])
    return result[index].tolist()[0]