# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:46:17 2018

@author: stweis
"""

# <codecell>

import numpy as np
import pandas as pd
import random
import scipy.stats as stats
import matplotlib.pyplot as plt


random.seed()


def simDPrime(trials=100,sameRate=.5,guessRate=.5):

    # simDPrime simulates D-prime for a set of [trials]. 
    # sameRate is the rate at which the answer should be "1" (a hit)
    # guessRate is the rate at which the guess will be a "1" 
    
    truth = pd.Series()
    guess = pd.Series()
    hits = 0
    fas = 0

    for i in range(trials):
        val = random.uniform(0.0,1.0)
        if val > sameRate:
            truth[i,] = 1
        else:
            truth[i,] = 0
        val2 = random.uniform(0.0,1.0)
        if val2 > (1-guessRate):
            guess[i,] = 1
        else:
            guess[i,] = 0
            
        if truth[i] == 1 and guess[i] == 1:
            hits += 1
        elif truth[i] == 0 and guess[i] == 1:
            fas += 1
                

    corrects = np.sum(truth)
    incorrects = 100 - corrects

    hitRate = hits / corrects
    faRate = fas / incorrects
    
    #Adjust for wonky values
    if hitRate <= .00001:
        hitRate = .001
    elif hitRate >= .99999:
        hitRate = .999
    if faRate <= .000001:
        faRate = .001
    elif faRate >= .99999:
        faRate = .999

    dPrime = stats.norm.ppf(hitRate) - stats.norm.ppf(faRate)

    return dPrime,hitRate,faRate

dPrimeIters = pd.Series()
hitRateIters = pd.Series()
faRateIters = pd.Series()

for i in range(100):
    dPrimeIters[i,],hitRateIters[i,],faRateIters[i,] = simDPrime(sameRate=.2,guessRate=.2)
    
n,bins,patches = plt.hist(dPrimeIters,20)   
print(np.mean(dPrimeIters))