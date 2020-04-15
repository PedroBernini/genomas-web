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


def getAllSigmas(permutation):
    return [applyReversal(permutation, rev[0], rev[1]) for rev in getAllReversals(len(permutation))]


def getAllScores(model):
    return [[(permutation, sigma, model.predict(np.array([join(permutation, sigma)]))[0][0]) for sigma in getAllSigmas(permutation)] for permutation in getAllPermutations(3)]


def getSigmasProtectionBreakPoint(permutation):
    return [applyReversal(permutation, rev[0], rev[1]) for rev in getAllReversals(len(permutation)) if rev[0] in breakpoints and (rev[1] + 1) in getAllBreakPoints(permutation)]


def getNumberBreakPoints(permutation) :
    return len(getAllBreakPoints)


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
    permutation = list(permutation)
    if(i > j):
        i, j = j, i
    strip = [permutation[k] for k in range(i, j + 1)]
    strip.reverse()
    for k in range(i, j + 1):
        permutation[k] = strip[k - i]
    return permutation


def nextByPermutationMarkovDecisionProcess(choices, intention, temperature):
    if choices == []:
        return intention
    temperature = temperature / 100
    result = np.array([intention, random.choice(choices)])
    index = np.random.choice(a = [0, 1], size = 1, replace = True, p = [temperature, 1 - temperature])
    return result[index].tolist()[0]