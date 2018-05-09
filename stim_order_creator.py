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

def stim_within_format_order(num_blocks=9,num_exemplars=21):
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

    print('There are {} matches'.format(np.sum(final_order['match'])))
    
    final_order = final_order[['direction','format','number']]
    
    final_order['Stimulus_stem'] = final_order.apply('_'.join,axis=1)

    return final_order[['direction','format','number','Stimulus_stem']]


final_within_whi_order = stim_within_format_order()
final_within_scr_order = stim_within_format_order()


def add_whi_suffix(row):
    newrow = row + '_WHI.jpg'
    return newrow

def add_scr_suffix(row):
    newrow = row + '_SCR.jpg'
    return newrow

final_within_whi_order['Stimulus'] = final_within_whi_order['Stimulus_stem'].apply(add_whi_suffix)
final_within_scr_order['Stimulus'] = final_within_scr_order['Stimulus_stem'].apply(add_scr_suffix)

final_within_whi_order.to_csv('vva_within_whi_order.csv',columns=['direction','format','number','Stimulus'],index=False)
final_within_scr_order.to_csv('vva_within_scr_order.csv',columns=['direction','format','number','Stimulus'],index=False)





