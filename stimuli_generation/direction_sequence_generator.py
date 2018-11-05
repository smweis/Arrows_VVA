# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:03:11 2018

This code will generate a sequence of 18 blocks of 10 trials each, with each trial
consisting of 2 stimuli. 

Each block of 20 trials will be the same format (images, schemas, words).

Each stimulus will be either 'left', 'right', or 'ahead.' 

Stimulus sequence is balanced for exactly the same number per format (120), 
approximately the same number of spatial direction (max = 125). 
Each stimulus will not appear more than 4 times in a row. 

Spatial direction number is balanced within format so that no spatial direction 
occurs more than 42 times per format. 

@author: stweis
"""
# <codecell>

import itertools
import operator
import random
import numpy as np
import pandas as pd
from toolz import interleave

dirs = ['l','a','r']
sequence = []

random.shuffle(dirs)

NUMBER_OF_TRIALS = 60

dirsOne = np.repeat(dirs, NUMBER_OF_TRIALS//3)
dirsTwo = np.repeat(dirs, NUMBER_OF_TRIALS//3)
sameDiff = np.repeat('notDone',NUMBER_OF_TRIALS)
final_order = np.vstack((dirsOne,dirsTwo,sameDiff)).T
final_order = pd.DataFrame(final_order,columns=('dirsOne','dirsTwo','sameDiff'))



def checkSame(first,second):
    if first == second:
        return 'same'
    else:
        return 'diff'
    

def checkPreviousTwoTrials(oneBack,twoBack):
    oneBackSameDiff = checkSame(final_order['dirsOne'][oneBack],final_order['dirsTwo'][oneBack])
    twoBackSameDiff = checkSame(final_order['dirsOne'][twoBack],final_order['dirsTwo'][twoBack])
    
    if oneBackSameDiff == twoBackSameDiff:
        return True
    else:
        return False
        
        
def sequenceGenerator():
    for i in range(NUMBER_OF_TRIALS):
        tempdirs = dirs
        random.shuffle(tempdirs) # shuffle the three dirs each time
        
        if i < 3: #first the first two trials, just generate random same/diff pairs
            randomSameDiff = random.randint(0,1)
        
            if randomSameDiff == 0:
                final_order['dirsOne'][i] = tempdirs[0]
                final_order['dirsTwo'][i] = tempdirs[0]
            else:
                final_order['dirsOne'][i] = tempdirs[0]
                final_order['dirsTwo'][i] = tempdirs[1]
            
        elif checkPreviousTwoTrials(i-1,i-2): #after the first two, check what the previous two were.
            if final_order['sameDiff'][i-1] == 'same': #if they were the same, do a diff
                final_order['dirsOne'][i] = tempdirs[0]
                final_order['dirsTwo'][i] = tempdirs[1]
            else: # else, if they were diff, do a same
                final_order['dirsOne'][i] = tempdirs[0]
                final_order['dirsTwo'][i] = tempdirs[0]
        
        else: #if it's not the first two trials, and the two previous were not both same or both different, generate a random same/diff pair
            randomSameDiff = random.randint(0,1)
            if randomSameDiff == 0:
                final_order['dirsOne'][i] = tempdirs[0]
                final_order['dirsTwo'][i] = tempdirs[0]
            else:
                final_order['dirsOne'][i] = tempdirs[0]
                final_order['dirsTwo'][i] = tempdirs[1]        
        
        # put same/diff
        final_order['sameDiff'][i] = checkSame(final_order['dirsOne'][i],final_order['dirsTwo'][i])
        
        
    maxdirOnedf = final_order.groupby(['dirsOne']).count()
    maxdirTwodf = final_order.groupby(['dirsTwo']).count()
    maxdirOne = maxdirOnedf['dirsTwo'].max()
    maxdirTwo = maxdirTwodf['dirsOne'].max()
    return(maxdirOne, maxdirTwo,final_order)



def cleanUp(order):
    new_order = pd.DataFrame(interleave([order['dirsOne'],order['dirsTwo']]),columns=['answer'])
    new_order['direction'] = 'notDone'
    for i in range(len(new_order)):
        if new_order['answer'][i] == 'r':
            new_order['direction'][i] = 'right'
        elif new_order['answer'][i] == 'a':
            new_order['direction'][i] = 'ahead'
        else:
            new_order['direction'][i] = 'left'
    return(new_order)
          

def generateOneFormatSequence():
    for i in range(1):
        a,b,participant_order = sequenceGenerator()
        cleanParticipantOrder = cleanUp(participant_order)
        
        
        rSeq = max((list(y) for (x,y) in itertools.groupby((enumerate(cleanParticipantOrder['answer'])),operator.itemgetter(1)) if x == 'a'), key=len)
        bSeq = max((list(y) for (x,y) in itertools.groupby((enumerate(cleanParticipantOrder['answer'])),operator.itemgetter(1)) if x == 'r'), key=len)
        oSeq = max((list(y) for (x,y) in itertools.groupby((enumerate(cleanParticipantOrder['answer'])),operator.itemgetter(1)) if x == 'l'), key=len)
        
        counter = 0
        
        
        
        # restrict the length of same dir in a row to 4; restrict the balance of dirs to be no worse than one dir appearing 21 times.
        while any(x > 3 for x in [len(rSeq),len(bSeq),len(oSeq)]) or max(a,b) > 21:
            a,b,participant_order = sequenceGenerator()
            cleanParticipantOrder = cleanUp(participant_order)
            
            rSeq = max((list(y) for (x,y) in itertools.groupby((enumerate(cleanParticipantOrder['answer'])),operator.itemgetter(1)) if x == 'a'), key=len)
            bSeq = max((list(y) for (x,y) in itertools.groupby((enumerate(cleanParticipantOrder['answer'])),operator.itemgetter(1)) if x == 'r'), key=len)
            oSeq = max((list(y) for (x,y) in itertools.groupby((enumerate(cleanParticipantOrder['answer'])),operator.itemgetter(1)) if x == 'l'), key=len)
        
            counter += 1
            if counter % 100 == 0:
                print('{}% done'.format(counter/100))
            if counter > 100000:
                print('Could not converge this time.')
                break


    print('Iterations:{}; Max in a row:{}, Max first stim: {}; Max second stim: {}'.format(counter,max(len(rSeq),len(oSeq),len(bSeq)),a,b))

    return cleanParticipantOrder


         
        
# Run the sequence three times, once for each format, balancing for the total number of stimuli being < 126 per format.
def finishSequence():
    formats = ['image','schema','word']     # which formats?     
    oneFormatOrder = pd.DataFrame()
    cleanParticipantOrder = pd.DataFrame()


    for i in formats:
        oneFormatOrder = generateOneFormatSequence()
        oneFormatOrder['format'] = i
        cleanParticipantOrder = cleanParticipantOrder.append(oneFormatOrder,ignore_index=True)


    while max(cleanParticipantOrder.groupby('direction').count()['format']) > 125:
        print(max(cleanParticipantOrder.groupby('direction').count()['format']))
        cleanParticipantOrder = pd.DataFrame()
        for i in formats:
            oneFormatOrder = generateOneFormatSequence()
            oneFormatOrder['format'] = i
            cleanParticipantOrder = cleanParticipantOrder.append(oneFormatOrder,ignore_index=True)


    num_blocks = 18
    num_exemplars = 21

    exemplar_numbers = np.arange(1,num_exemplars+1).tolist() 
    random.shuffle(exemplar_numbers)

    all_exemplars = []

    for i in range(0,num_blocks):
        all_exemplars = np.append(all_exemplars,exemplar_numbers,axis=0)
        random.shuffle(exemplar_numbers) #shuffle these each time


    cleanParticipantOrder['number'] = 999

    all_format_orders = list(itertools.permutations(formats))
    random.shuffle(all_format_orders)

    selected_orders = np.reshape(all_format_orders,num_blocks)
    final_format_order = np.repeat(selected_orders,num_exemplars-1)

    r_i_exemplars = all_exemplars[0:42]
    l_i_exemplars = all_exemplars[42:84]
    a_i_exemplars = all_exemplars[84:126]
    
    r_s_exemplars = all_exemplars[126:168]
    l_s_exemplars = all_exemplars[168:210]
    a_s_exemplars = all_exemplars[210:252]
    
    r_w_exemplars = all_exemplars[252:294]
    l_w_exemplars = all_exemplars[294:336]
    a_w_exemplars = all_exemplars[336:378]
    
    r_i_counter = 0   
    l_i_counter = 0
    a_i_counter = 0
    
    r_s_counter = 0   
    l_s_counter = 0
    a_s_counter = 0
    
    r_w_counter = 0   
    l_w_counter = 0
    a_w_counter = 0
    
    for i in range(len(cleanParticipantOrder)):
        if cleanParticipantOrder['format'][i] == 'image':
            if cleanParticipantOrder['answer'][i] == 'r':
                cleanParticipantOrder['number'][i] = r_i_exemplars[r_i_counter]
                r_i_counter += 1
            elif cleanParticipantOrder['answer'][i] == 'l':
                cleanParticipantOrder['number'][i] = l_i_exemplars[l_i_counter]
                l_i_counter += 1
            elif cleanParticipantOrder['answer'][i] == 'a':
                cleanParticipantOrder['number'][i] = a_i_exemplars[a_i_counter]
                a_i_counter += 1
        elif cleanParticipantOrder['format'][i] == 'schema':
            if cleanParticipantOrder['answer'][i] == 'r':
                cleanParticipantOrder['number'][i] = r_s_exemplars[r_s_counter]
                r_s_counter += 1
            elif cleanParticipantOrder['answer'][i] == 'l':
                cleanParticipantOrder['number'][i] = l_s_exemplars[l_s_counter]
                l_s_counter += 1
            elif cleanParticipantOrder['answer'][i] == 'a':
                cleanParticipantOrder['number'][i] = a_s_exemplars[a_s_counter]
                a_s_counter += 1
        elif cleanParticipantOrder['format'][i] == 'word':
            if cleanParticipantOrder['answer'][i] == 'r':
                cleanParticipantOrder['number'][i] = r_w_exemplars[r_w_counter]
                r_w_counter += 1
            elif cleanParticipantOrder['answer'][i] == 'l':
                cleanParticipantOrder['number'][i] = l_w_exemplars[l_w_counter]
                l_w_counter += 1
            elif cleanParticipantOrder['answer'][i] == 'a':
                cleanParticipantOrder['number'][i] = a_w_exemplars[a_w_counter]
                a_w_counter += 1 

    cleanParticipantOrder['formatOrder'] = 999

    w_counter = 0
    s_counter = 0
    i_counter = 0

    for i in range(len(selected_orders)):
        if selected_orders[i] == 'word':
            cleanParticipantOrder['formatOrder'][240+(20*w_counter):260+(20*w_counter)] = i
            w_counter+= 1
        elif selected_orders[i] == 'schema':
            cleanParticipantOrder['formatOrder'][120+(20*s_counter):140+(20*s_counter)] = i
            s_counter += 1
        else:
            cleanParticipantOrder['formatOrder'][20*i_counter:20+(20*i_counter)] = i
            i_counter += 1

    cleanParticipantOrder['index'] = cleanParticipantOrder.index
    cleanParticipantOrder.sort_values(['formatOrder','index'],inplace=True)



    cleanParticipantOrder = cleanParticipantOrder[['direction','format','number']]    
    cleanParticipantOrder['number'] = cleanParticipantOrder['number'].astype(int).astype(str)

    cleanParticipantOrder['Stimulus_stem'] = cleanParticipantOrder.apply('_'.join,axis=1)


    return cleanParticipantOrder


    


def add_whi_suffix(row):
    newrow = row + '_WHI.jpg'
    return newrow


def add_scr_suffix(row):
    newrow = row + '_SCR.jpg'
    return newrow



for i in range(14):     
    newOrder = finishSequence()

    participant_num = 1001+i
    filename = str(participant_num) + 'vva_within_whi_order.csv'
    newOrder['Stimulus'] = newOrder['Stimulus_stem'].apply(add_whi_suffix)

    newOrder.to_csv(filename,columns=['direction','format','number','Stimulus'],index=False)


