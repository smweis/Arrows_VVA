# -*- coding: utf-8 -*-
"""
Created on Tue May  1 13:20:30 2018

@author: stweis
"""
# <codecell>
from psychopy import visual, core

win = visual.Window()
msg = visual.TextStim(win, text=u"\u00A1Hola mundo!")

msg.draw()
win.flip()
core.wait(1)
win.close()