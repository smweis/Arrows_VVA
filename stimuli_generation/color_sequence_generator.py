# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:03:11 2018

@author: stweis
"""
# <codecell>

import itertools
import operator
import random
import numpy as np
import pandas as pd
from toolz import interleave

colors = ['r','o','b']
sequence = []

random.shuffle(colors)

NUMBER_OF_TRIALS = 60

colorsOne = np.repeat(colors, NUMBER_OF_TRIALS//3)
colorsTwo = np.repeat(colors, NUMBER_OF_TRIALS//3)
sameDiff = np.repeat('notDone',NUMBER_OF_TRIALS)
final_order = np.vstack((colorsOne,colorsTwo,sameDiff)).T
final_order = pd.DataFrame(final_order,columns=('colorsOne','colorsTwo','sameDiff'))



def checkSame(first,second):
    if first == second:
        return 'same'
    else:
        return 'diff'
    

def checkPreviousTwoTrials(oneBack,twoBack):
    oneBackSameDiff = checkSame(final_order['colorsOne'][oneBack],final_order['colorsTwo'][oneBack])
    twoBackSameDiff = checkSame(final_order['colorsOne'][twoBack],final_order['colorsTwo'][twoBack])
    
    if oneBackSameDiff == twoBackSameDiff:
        return True
    else:
        return False
        
        
def sequenceGenerator():
    for i in range(NUMBER_OF_TRIALS):
        tempColors = colors
        random.shuffle(tempColors) # shuffle the three colors each time
        
        if i < 3: #first the first two trials, just generate random same/diff pairs
            randomSameDiff = random.randint(0,1)
        
            if randomSameDiff == 0:
                final_order['colorsOne'][i] = tempColors[0]
                final_order['colorsTwo'][i] = tempColors[0]
            else:
                final_order['colorsOne'][i] = tempColors[0]
                final_order['colorsTwo'][i] = tempColors[1]
            
        elif checkPreviousTwoTrials(i-1,i-2): #after the first two, check what the previous two were.
            if final_order['sameDiff'][i-1] == 'same': #if they were the same, do a diff
                final_order['colorsOne'][i] = tempColors[0]
                final_order['colorsTwo'][i] = tempColors[1]
            else: # else, if they were diff, do a same
                final_order['colorsOne'][i] = tempColors[0]
                final_order['colorsTwo'][i] = tempColors[0]
        
        else: #if it's not the first two trials, and the two previous were not both same or both different, generate a random same/diff pair
            randomSameDiff = random.randint(0,1)
            if randomSameDiff == 0:
                final_order['colorsOne'][i] = tempColors[0]
                final_order['colorsTwo'][i] = tempColors[0]
            else:
                final_order['colorsOne'][i] = tempColors[0]
                final_order['colorsTwo'][i] = tempColors[1]        
        
        # put same/diff
        final_order['sameDiff'][i] = checkSame(final_order['colorsOne'][i],final_order['colorsTwo'][i])
        
        
    maxColorOnedf = final_order.groupby(['colorsOne']).count()
    maxColorTwodf = final_order.groupby(['colorsTwo']).count()
    maxColorOne = maxColorOnedf['colorsTwo'].max()
    maxColorTwo = maxColorTwodf['colorsOne'].max()
    return(maxColorOne, maxColorTwo,final_order)



def cleanUp(order):
    new_order = pd.DataFrame(interleave([order['colorsOne'],order['colorsTwo']]),columns=['answer'])
    new_order['color'] = 'notDone'
    for i in range(len(new_order)):
        if new_order['answer'][i] == 'r':
            new_order['color'][i] = '#d7191c'
        elif new_order['answer'][i] == 'o':
            new_order['color'][i] = '#fdae61'
        else:
            new_order['color'][i] = '#2c7bb6'
    return(new_order)
          



### Run sequence generator until we have approximately equal coverage of each color

for i in range(14):
    a,b,participant_order = sequenceGenerator()
    cleanParticipantOrder = cleanUp(participant_order)
    
    
    rSeq = max((list(y) for (x,y) in itertools.groupby((enumerate(cleanParticipantOrder['answer'])),operator.itemgetter(1)) if x == 'r'), key=len)
    bSeq = max((list(y) for (x,y) in itertools.groupby((enumerate(cleanParticipantOrder['answer'])),operator.itemgetter(1)) if x == 'b'), key=len)
    oSeq = max((list(y) for (x,y) in itertools.groupby((enumerate(cleanParticipantOrder['answer'])),operator.itemgetter(1)) if x == 'o'), key=len)
    
    counter = 0
    
    
    # restrict the length of same color in a row to 4; restrict the balance of colors to be no worse than one color appearing 23 times.
    while any(x > 3 for x in [len(rSeq),len(bSeq),len(oSeq)]) or max(a,b) > 21:
        a,b,participant_order = sequenceGenerator()
        cleanParticipantOrder = cleanUp(participant_order)
        
        rSeq = max((list(y) for (x,y) in itertools.groupby((enumerate(cleanParticipantOrder['answer'])),operator.itemgetter(1)) if x == 'r'), key=len)
        bSeq = max((list(y) for (x,y) in itertools.groupby((enumerate(cleanParticipantOrder['answer'])),operator.itemgetter(1)) if x == 'b'), key=len)
        oSeq = max((list(y) for (x,y) in itertools.groupby((enumerate(cleanParticipantOrder['answer'])),operator.itemgetter(1)) if x == 'o'), key=len)
    
        counter += 1
        if counter % 1000 == 0:
            print('{}% done'.format(counter/1000))
        if counter > 1000000:
            print('Could not converge this time.')
            break
        
    print('Iterations:{}; Max in a row:{}, Max first stim: {}; Max second stim: {}'.format(counter,max(len(rSeq),len(oSeq),len(bSeq)),a,b))
        
        
        
    participant_num = 1001+i
    filename = str(participant_num) + 'color_order.csv'
    cleanParticipantOrder.to_csv(filename,columns=['answer','color'],index=False)


