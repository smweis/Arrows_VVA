# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 12:46:43 2018

@author: stweis

Goal is to create a list of trials, randomized by block, direction, and 
stimulus number, with a few constraints. 
"""

# <codecell>

import itertools
import random
import numpy as np
import pandas as pd

def stim_within_format_order(num_blocks=18,num_exemplars=21):
	# num_blocks: how many within-format blocks?
	# num_exemplars: how many exemplars per format+direction? 
	# defaults are for the VVA design

    directions = ['left','right','ahead']   # which directions?
    random.shuffle(directions)

    formats = ['image','schema','word']     # which formats?     
    random.shuffle(formats)

    exemplar_numbers = np.arange(1,num_exemplars+1).tolist() 
    random.shuffle(exemplar_numbers)



    all_format_orders = list(itertools.permutations(formats))
    random.shuffle(all_format_orders)
    #These are hard-coded to select a counter-balanced set of orders
    #selected_orders = all_format_orders[0], all_format_orders[3], all_format_orders[4]

    selected_orders = np.reshape(all_format_orders,num_blocks)
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

    matches = np.sum(final_order['match'][1::2])
    
    final_order = final_order[['direction','format','number']]
    
    final_order['Stimulus_stem'] = final_order.apply('_'.join,axis=1)
    #debug print('we are trying...', matches)
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
# Running this 10000 times yielded M: 113.74, SD: 8.98

#for i in range(10000):
#    if i % 100 == 0:
#        print(i)
#    final_within_whi_order,match_whi = stim_within_format_order()
#    matches_whi.append(match_whi)
#print("WHI match mean: {} +/- {}".format(np.mean(matches_whi),np.std(matches_whi)))
#print("WHI max = {}, min = {}".format(max(matches_whi),min(matches_whi)))


match_max = 57.03 + 6.53 #exclusive
match_min = 57.03 - 6.53 #exclusive
"""
for i in range(14):
    participant_num = 1001+i
    filename_whi = str(participant_num) + 'vva_within_whi_order.csv'
    filename_scr = str(participant_num) + 'vva_within_scr_order.csv'
    
        
    final_within_whi_order,match_whi = stim_within_format_order()
    final_within_scr_order,match_scr = stim_within_format_order()
    
    while match_whi <= match_min or match_whi >= match_max: 
        final_within_whi_order,match_whi = stim_within_format_order()
        
    while match_scr <= match_min or match_scr > match_max:
        final_within_scr_order,match_scr = stim_within_format_order()

        
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