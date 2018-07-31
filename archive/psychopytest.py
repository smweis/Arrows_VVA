# -*- coding: utf-8 -*-
"""
Created on Tue May  1 13:20:30 2018

@author: stweis
"""
# <codecell>
from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0, color=[1,1,1], colorSpace='rgb')

msg = visual.TextStim(win, text=u"\u00A1Hola mundo!", color=[0,0,0])

msg.draw()
win.flip()
core.wait(1)
win.close()
