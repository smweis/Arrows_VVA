# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 12:46:43 2018

@author: stweis

Goal is to create a list of trials, randomized by block, direction, and 
stimulus number, with a few constraints. 

Same as stim_order_creator.py except here we're creating an order that 
is all cross-format. 
"""

# <codecell>

import itertools
import random
import numpy as np
import pandas as pd

#def stim_across_format_order(num_blocks=9,num_exemplars=21):

	# num_exemplars: how many exemplars per format+direction? 
	# defaults are for the VVA design

def makeTools():
    names = [['image','image','image','schema','schema','schema','word','word','word'],
             ['left','right','ahead','left','right','ahead','left','right','ahead']]

    number_of_trials = 189 # to match within format trial number

    stim_names = list(zip(*names))

    stimuli = {}

    for i in stim_names:
        temp = list(range(1,22))
        random.shuffle(temp)
        temp2 = temp[0:7],temp[7:14],temp[14:21]
        stimuli[i] = temp2
    
    return names,number_of_trials,stim_names,stimuli


def chooseFormat(formats,block):
    #stim_names global variable
    #stimuli global variable 
    
    stim_names_temp = stim_names[:]
    
    for key,value in stimuli.items():                      
        if not value[block]:                
            stim_names_temp.remove(key)
            
            
    images = []
    schemas = []
    words = []
    
    for i in stim_names_temp:
        if 'image' in i:
            images.append(i)
        elif 'schema' in i:
            schemas.append(i)
        elif 'word' in i:
            words.append(i)
        
    if 'all' in formats:
        trial_list = images + schemas + words
    elif 'image' in formats:
        trial_list = schemas + words
    elif 'schema' in formats:
        trial_list = images + words
    elif 'word' in formats:
        trial_list = images + schemas

    #if not trial_list:
    #    trial_list = images + schemas + words
    #    print('there are repeats at the end')
    
    trial_type = random.choice(trial_list)

    format_type = trial_type[0]
    direction = trial_type[1]
    num = stimuli[trial_type][block].pop()
    stimulus = direction + '_' + format_type + '_' + str(num)
    
    

    return format_type,direction,num,stimulus




def makeTrials():
    

    
    trials = pd.DataFrame()

    for i in range(0,number_of_trials):   
        if i == 0:
            trials.at[i,'format'],trials.at[i,'direction'],trials.at[i,'num'],trials.at[i,'stimulus'] = chooseFormat('all',0)
        elif i < 63:
            trials.at[i,'format'],trials.at[i,'direction'],trials.at[i,'num'],trials.at[i,'stimulus'] = chooseFormat(trials.loc[i-1,'format'],0)
        elif i < 126:
            trials.at[i,'format'],trials.at[i,'direction'],trials.at[i,'num'],trials.at[i,'stimulus'] = chooseFormat(trials.loc[i-1,'format'],1)
        else:
            trials.at[i,'format'],trials.at[i,'direction'],trials.at[i,'num'],trials.at[i,'stimulus'] = chooseFormat(trials.loc[i-1,'format'],2)
    return trials



for i in range(100):
    names,number_of_trials,stim_names,stimuli = makeTools()
    try:
        trials = makeTrials()
        break
    except IndexError:
        continue


        
#while trials is None:
#    try:
#     trials = makeTrials()
#    except IndexError:
#        'damn'
    



# <codecell>
"""
    
    
    directions = ['left','right','ahead']   # which directions?
    random.shuffle(directions)

    formats = ['image','schema','word']     # which formats?     
    random.shuffle(formats)

    exemplar_numbers = np.arange(1,num_exemplars+1).tolist() 
    random.shuffle(exemplar_numbers)



    all_format_orders = list(itertools.permutations(formats))

    #These are hard-coded to select a counter-balanced set of orders
    selected_orders = all_format_orders[0], all_format_orders[3], all_format_orders[4]

    selected_orders = np.reshape(selected_orders,num_blocks)
    final_format_order = np.repeat(selected_orders,num_exemplars)


    all_exemplars = []


    for i in range(0,num_blocks):
        all_exemplars = np.append(all_exemplars,exemplar_numbers,axis=0)
        random.shuffle(exemplar_numbers) #shuffle these each time
    



    final_direction_order = []

    for i in range(0,num_blocks):
        all_directions = np.repeat(directions, num_exemplars//3)
        random.shuffle(all_directions)
        final_direction_order.append(all_directions)
    

    final_direction_order = np.reshape(final_direction_order,num_exemplars*num_blocks)


    final_order = np.vstack((final_format_order,final_direction_order)).T

    final_order = pd.DataFrame(final_order,columns=('format','direction'))
    final_order.sort_values(by=['format','direction'],inplace=True)
    final_order['number'] = all_exemplars
    final_order['number'] = final_order['number'].astype(int).astype(str)

    final_order.sort_index(inplace=True)
    

    final_order['match'] = final_order.direction.eq(final_order.direction.shift())

    matches = np.sum(final_order['match'])
    
    final_order = final_order[['direction','format','number']]
    
    final_order['Stimulus_stem'] = final_order.apply('_'.join,axis=1)

    return final_order[['direction','format','number','Stimulus_stem']],matches


def add_whi_suffix(row):
    newrow = row + '_WHI.jpg'
    return newrow

def add_scr_suffix(row):
    newrow = row + '_SCR.jpg'
    return newrow


matches_whi = []
matches_scr = []



# Establish the mean and SD of the number of matches for a sequence
# We'll use any sequences that have a number of matches within 1 SD of the mean
# Running this 10000 times yielded M: 56.62, SD: 6.35

#for i in range(10000):
#    final_within_whi_order,match_whi = stim_within_format_order()
#    matches_whi.append(match_whi)
#print("WHI match mean: {} +/- {}".format(np.mean(matches_whi),np.std(matches_whi)))
#print("WHI max = {}, min = {}".format(max(matches_whi),min(matches_whi)))


match_max = 63 #exclusive
match_min = 50 #exclusive

for i in range(14):
    participant_num = 1001+i
    filename_whi = str(participant_num) + 'vva_within_whi_order.csv'
    filename_scr = str(participant_num) + 'vva_within_scr_order.csv'
    
        
    final_within_whi_order,match_whi = stim_across_format_order()
    final_within_scr_order,match_scr = stim_across_format_order()
    
    while match_whi <= match_min or match_whi >= match_max: 
        final_within_whi_order,match_whi = stim_across_format_order()
        
    while match_scr <= match_min or match_scr > match_max:
        final_within_scr_order,match_scr = stim_across_format_order()

        
    final_within_whi_order['Stimulus'] = final_within_whi_order['Stimulus_stem'].apply(add_whi_suffix)
    final_within_scr_order['Stimulus'] = final_within_scr_order['Stimulus_stem'].apply(add_scr_suffix)
    final_within_whi_order.to_csv(filename_whi,columns=['direction','format','number','Stimulus'],index=False)
    final_within_scr_order.to_csv(filename_scr,columns=['direction','format','number','Stimulus'],index=False)
    matches_whi.append(match_whi)
    matches_scr.append(match_scr)
        

print("SCR match mean: {} +/- {}".format(np.mean(matches_scr),np.std(matches_scr)))
print("SCR max = {}, min = {}".format(max(matches_scr),min(matches_scr)))
print("WHI match mean: {} +/- {}".format(np.mean(matches_whi),np.std(matches_whi)))
print("WHI max = {}, min = {}".format(max(matches_whi),min(matches_whi)))
"""