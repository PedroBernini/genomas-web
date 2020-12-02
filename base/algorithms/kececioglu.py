# The Greedy Algorithm - Kececioglu
# Autor: Pedro Henrique Bernini Silva

import sys
import os


def isAdjacent(a, b) :
    if (abs(a - b) == 1) :
        return True
    else :
        return False

def breakPoints(permutation, bkpMap) :
    bkpMap.clear()
    breakPoints = 0
    for i in range(0, len(permutation)-1) :
        if (isAdjacent(permutation[i+1], permutation[i]) is False):
            breakPoints += 1
            bkpMap.append((i,i+1))
    return breakPoints

def hasDecreasingStrip(permutation, bkpMap) :
    stripDecreasing = False
    for i in range(0, len(bkpMap) - 1) :
        start = bkpMap[i][1]
        end = bkpMap[i+1][0]
        if start == end :
            stripDecreasing = True
            break
        elif (permutation[start] - permutation[start + 1] == 1):
            stripDecreasing = True
            break
    return stripDecreasing

def takeSmallestElement(permutation, bkpMap) :
    smaller = len(permutation)
    for i in range(0, len(bkpMap) - 1) :
        start = bkpMap[i][1]
        end = bkpMap[i+1][0]
        if start == end and permutation[start] < smaller :
            smaller = permutation[start]
        elif (permutation[start] - permutation[start + 1] == 1) :
            while start <= end :
                if permutation[start] < smaller :
                    smaller = permutation[start]
                start += 1
    return smaller

def takeBiggestElement(permutation, bkpMap) :
    bigger = 0
    for i in range(0, len(bkpMap) - 1) :
        start = bkpMap[i][1]
        end = bkpMap[i+1][0]
        if start == end and permutation[start] > bigger :
            bigger = permutation[start]
        elif (permutation[start] - permutation[start + 1] == 1) :
            while start <= end :
                if permutation[start] > bigger :
                    bigger = permutation[start]
                start += 1
    return bigger

def reversal(i, j, permutation) :
    resultReversal = list(permutation)
    strip = []
    if(i>j) :
        temp = i
        i = j
        j = temp
    for k in range(i,j+1) :
        strip.append(resultReversal[k]) 
    strip.reverse();
    for k in range(i,j+1) :
        resultReversal[k] = strip[k-i]
    return resultReversal
   

def getDistanceToIdentity(permutation):
    permutation = [0] + permutation + [len(permutation) + 1]
    bkpMap = []
    Permutations = [list(permutation)]
    reversoes = 0
    while(breakPoints(permutation, bkpMap) > 0):
        
        resultReversal = None
        if hasDecreasingStrip(permutation, bkpMap):
            # Encontrar o menor elemento de strip decrescente
            k = takeSmallestElement(permutation, bkpMap)   
            if permutation.index(k) < permutation.index(k - 1) :
                resultReversal = reversal(permutation.index(k)+1, permutation.index(k-1), permutation)
            else :
                resultReversal = reversal(permutation.index(k), permutation.index(k-1)+1, permutation)
            
            # Encontrar o maior elemento de strip decrescente
            breakPoints(resultReversal, bkpMap)
            if hasDecreasingStrip(resultReversal, bkpMap) == False :
                breakPoints(permutation, bkpMap)
                l = takeBiggestElement(permutation, bkpMap)
                if permutation.index(l) > permutation.index(l + 1) :
                    resultReversal = reversal(permutation.index(l)-1, permutation.index(l+1), permutation)
                else :
                    resultReversal = reversal(permutation.index(l), permutation.index(l+1)-1, permutation)
        else:
            resultReversal = reversal(bkpMap[0][1], bkpMap[1][0], permutation)
        
        permutation = resultReversal
        Permutations.append(list(permutation))
        reversoes += 1
        
    return reversoes

print(getDistanceToIdentity([3,1,4,2]))