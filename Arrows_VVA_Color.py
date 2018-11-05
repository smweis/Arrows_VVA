#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on November 02, 2018, at 16:01
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('1')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

psychopy.useVersion('1.76.00')


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'Arrows_VVA_Color'  # from the Builder filename that created this script
expInfo = {u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data_Arrows_VVA_Color' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[.4,.4,.4], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "color_instructions"
color_instructionsClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Your job is to determine whether two shapes are the SAME color, or DIFFERENT colors.\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "color_sample_same"
color_sample_sameClock = core.Clock()
polygon_2 = visual.Polygon(
    win=win, name='polygon_2',units='height', 
    edges=999, size=(0.5, .5),
    ori=0, pos=(-.3, -.2),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='#d7191c', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3',units='height', 
    vertices=[[-(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [+(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [0,(0.5, 0.5)[1]/2.0]],
    ori=0, pos=(.3, -.2),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='#d7191c', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
text_3 = visual.TextStim(win=win, name='text_3',
    text='These shapes are the SAME color. If you saw the shape on the left followed by the shape on the right, you would say \n\n        "SAME"',
    font='Arial',
    units='norm', pos=(0, .6), height=0.1, wrapWidth=1, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "color_sample_diff"
color_sample_diffClock = core.Clock()
polygon_4 = visual.Polygon(
    win=win, name='polygon_4',units='height', 
    edges=5, size=(0.5, 0.5),
    ori=0, pos=(.3, -.2),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='#fdae61', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
polygon_5 = visual.Polygon(
    win=win, name='polygon_5',units='height', 
    edges=5, size=(0.5, 0.5),
    ori=0, pos=(-.3, -.2),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='#2c7bb6', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
text_5 = visual.TextStim(win=win, name='text_5',
    text='These shapes are DIFFERENT colors. If you saw the shape on the left followed by the shape on the right, you would say \n\n        "DIFFERENT"',
    font='Arial',
    pos=(0, .6), height=0.1, wrapWidth=1, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "color_practice_instructions"
color_practice_instructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
import random

colorOrder = expInfo['participant'] + 'color_order.csv'

if random.randint(0,1) == 0:
    colorPracticeOrder1 = 'color_practice_1.csv'
    colorPracticeOrder2 = 'color_practice_2.csv'
else:
    colorPracticeOrder1 = 'color_practice_2.csv'
    colorPracticeOrder2 = 'color_practice_1.csv'

# Initialize components for Routine "color_practice"
color_practiceClock = core.Clock()
import random

vertexOptions = [3,4,5,6,999]
text_9 = visual.TextStim(win=win, name='text_9',
    text=None,
    font='Arial',
    pos=(0, -.6), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_same_practice = visual.TextStim(win=win, name='text_same_practice',
    text=None,
    font='Arial',
    pos=(0, -.8), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "color_instructions_3"
color_instructions_3Clock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='Great! Now for the actual experiment. You have as long as you like - try to get as many correct as you can.\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "color_trials"
color_trialsClock = core.Clock()
between_format_text = visual.TextStim(win, color='black',text="Ready for the next set?")
colorOrder = expInfo['participant'] + 'color_order.csv'
text_same = visual.TextStim(win=win, name='text_same',
    text=None,
    font='Arial',
    pos=(0, -.8), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "ISI_2"
ISI_2Clock = core.Clock()
fixation_2 = visual.TextStim(win=win, name='fixation_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "end"
endClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='This portion of the experiment is over. Thank you.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "color_instructions"-------
t = 0
color_instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
color_instructionsComponents = [text_4, key_resp_7]
for thisComponent in color_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "color_instructions"-------
while continueRoutine:
    # get current time
    t = color_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['s', 'a', 'd', 'f', 'g'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in color_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "color_instructions"-------
for thisComponent in color_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys=None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "color_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "color_sample_same"-------
t = 0
color_sample_sameClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
color_sample_sameComponents = [polygon_2, polygon_3, text_3, key_resp_8]
for thisComponent in color_sample_sameComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "color_sample_same"-------
while continueRoutine:
    # get current time
    t = color_sample_sameClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_2* updates
    if t >= 0 and polygon_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_2.tStart = t
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.setAutoDraw(True)
    
    # *polygon_3* updates
    if t >= 0.0 and polygon_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_3.tStart = t
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.setAutoDraw(True)
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['s', 'a', 'd', 'f', 'g'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in color_sample_sameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "color_sample_same"-------
for thisComponent in color_sample_sameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "color_sample_same" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "color_sample_diff"-------
t = 0
color_sample_diffClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()
# keep track of which components have finished
color_sample_diffComponents = [polygon_4, polygon_5, text_5, key_resp_9]
for thisComponent in color_sample_diffComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "color_sample_diff"-------
while continueRoutine:
    # get current time
    t = color_sample_diffClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_4* updates
    if t >= 0.0 and polygon_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_4.tStart = t
        polygon_4.frameNStart = frameN  # exact frame index
        polygon_4.setAutoDraw(True)
    
    # *polygon_5* updates
    if t >= 0.0 and polygon_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_5.tStart = t
        polygon_5.frameNStart = frameN  # exact frame index
        polygon_5.setAutoDraw(True)
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['s', 'a', 'd', 'f', 'g'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_9.keys = theseKeys[-1]  # just the last key pressed
            key_resp_9.rt = key_resp_9.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in color_sample_diffComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "color_sample_diff"-------
for thisComponent in color_sample_diffComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys=None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()
# the Routine "color_sample_diff" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
repeat_color_practice = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repeat_color_practice')
thisExp.addLoop(repeat_color_practice)  # add the loop to the experiment
thisRepeat_color_practice = repeat_color_practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeat_color_practice.rgb)
if thisRepeat_color_practice != None:
    for paramName in thisRepeat_color_practice:
        exec('{} = thisRepeat_color_practice[paramName]'.format(paramName))

for thisRepeat_color_practice in repeat_color_practice:
    currentLoop = repeat_color_practice
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat_color_practice.rgb)
    if thisRepeat_color_practice != None:
        for paramName in thisRepeat_color_practice:
            exec('{} = thisRepeat_color_practice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "color_practice_instructions"-------
    t = 0
    color_practice_instructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6 = event.BuilderKeyResponse()
    if repeat_color_practice.thisN == 0:
        text_6.setText("Let's try a few for practice. You'll see pairs of shapes, with one shape on the screen at a time. Each shape will be BLUE or RED or ORANGE. Tell me if the two shapes are the SAME color, or DIFFERENT colors. For the first shape, just say 'GO.' Then, when it says 'Same/Different?' underneath, tell me whether you see the same color or a different color as the first shape [Experimenter: Press Green for SAME, Red for DIFFERENT]")
        colorPracticeOrder = colorPracticeOrder1
    elif repeat_color_practice.thisN == 1:
        text_6.setText("Ok, before we practice one more time - do you have any questions about the task?")
        colorPracticeOrder = colorPracticeOrder2
    # keep track of which components have finished
    color_practice_instructionsComponents = [text_6, key_resp_6]
    for thisComponent in color_practice_instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "color_practice_instructions"-------
    while continueRoutine:
        # get current time
        t = color_practice_instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if t >= 0.0 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['s', 'd', 'g'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6.rt = key_resp_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in color_practice_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "color_practice_instructions"-------
    for thisComponent in color_practice_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys=None
    repeat_color_practice.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        repeat_color_practice.addData('key_resp_6.rt', key_resp_6.rt)
    
    # the Routine "color_practice_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("Sequences//"+ colorPracticeOrder),
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "color_practice"-------
        t = 0
        color_practiceClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_11 = event.BuilderKeyResponse()
        if trials_3.thisN == 0:
            lastTrialColor = thisTrial_3.answer
            lastnVertices = []
        
        if trials_3.thisN % 2 == 1:
            text_same_practice.setText("SAME / DIFFERENT?")
        else:
            text_same_practice.setText("")
        
        tempVerts = vertexOptions[:]
        
        try:
            tempVerts.remove(lastnVertices)
        except ValueError:
            pass
        
        nVertices = random.choice(tempVerts)
        
        
        
        poly = visual.Polygon(win=win,autoDraw = True,fillColor=thisTrial_3.color,edges=nVertices,units='height',size=[.5,.5])
        
        # keep track of which components have finished
        color_practiceComponents = [key_resp_11, text_9, text_same_practice]
        for thisComponent in color_practiceComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "color_practice"-------
        while continueRoutine:
            # get current time
            t = color_practiceClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_11* updates
            if t >= 0.0 and key_resp_11.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_11.tStart = t
                key_resp_11.frameNStart = frameN  # exact frame index
                key_resp_11.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if key_resp_11.status == STARTED:
                theseKeys = event.getKeys(keyList=['a', 'f'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_11.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_11.rt = key_resp_11.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            
            # *text_9* updates
            if t >= 0 and text_9.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_9.tStart = t
                text_9.frameNStart = frameN  # exact frame index
                text_9.setAutoDraw(True)
            
            # *text_same_practice* updates
            if t >= 0.0 and text_same_practice.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_same_practice.tStart = t
                text_same_practice.frameNStart = frameN  # exact frame index
                text_same_practice.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in color_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "color_practice"-------
        for thisComponent in color_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_11.keys in ['', [], None]:  # No response was made
            key_resp_11.keys=None
        trials_3.addData('key_resp_11.keys',key_resp_11.keys)
        if key_resp_11.keys != None:  # we had a response
            trials_3.addData('key_resp_11.rt', key_resp_11.rt)
        if trials_3.thisN == 0:
            correct = 1
        elif lastTrialColor == thisTrial_3.answer and key_resp_11.keys in ['a']:
            correct = 1
        elif lastTrialColor != thisTrial_3.answer and key_resp_11.keys in ['f']:
            correct = 1
        else:
            correct = 0
        
        lastTrialColor = thisTrial_3.answer
        
        lastnVertices = nVertices
        if trials_3.thisN % 2 == 1:
            trials_3.addData('colorpractice_correct',correct)
        
        trials_3.addData('colorpractice_numVertices',nVertices)
        
        poly.setAutoDraw(False)
        # the Routine "color_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ISI"-------
        t = 0
        ISIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if trials_3.thisN % 2 == 0:
            continueRoutine = False
        # keep track of which components have finished
        ISIComponents = [fixation]
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if t >= 0.0 and fixation.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation.tStart = t
                fixation.frameNStart = frameN  # exact frame index
                fixation.setAutoDraw(True)
            frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation.status == STARTED and t >= frameRemains:
                fixation.setAutoDraw(False)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_3'
    
    # get names of stimulus parameters
    if trials_3.trialList in ([], [None], None):
        params = []
    else:
        params = trials_3.trialList[0].keys()
    # save data for this loop
    trials_3.saveAsExcel(filename + '.xlsx', sheetName='trials_3',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed 2 repeats of 'repeat_color_practice'


# ------Prepare to start Routine "color_instructions_3"-------
t = 0
color_instructions_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_13 = event.BuilderKeyResponse()
# keep track of which components have finished
color_instructions_3Components = [text_10, key_resp_13]
for thisComponent in color_instructions_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "color_instructions_3"-------
while continueRoutine:
    # get current time
    t = color_instructions_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t
        text_10.frameNStart = frameN  # exact frame index
        text_10.setAutoDraw(True)
    
    # *key_resp_13* updates
    if t >= 0.0 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = event.getKeys(keyList=['s', 'd', 'g'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_13.keys = theseKeys[-1]  # just the last key pressed
            key_resp_13.rt = key_resp_13.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in color_instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "color_instructions_3"-------
for thisComponent in color_instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys=None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.nextEntry()
# the Routine "color_instructions_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("Sequences//"+ colorOrder),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "color_trials"-------
    t = 0
    color_trialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    color_response = event.BuilderKeyResponse()
    if trials_2.thisN == 0:
        lastTrialColor = thisTrial_2.answer
        lastnVertices = []
    
    if trials_2.thisN % 2 == 1:
        text_same.setText("SAME / DIFFERENT?")
    else:
        text_same.setText("")
    
    tempVerts = vertexOptions[:]
    
    try:
        tempVerts.remove(lastnVertices)
    except ValueError:
        pass
    
    nVertices = random.choice(tempVerts)
    
    
    poly = visual.Polygon(win=win,autoDraw = True,fillColor=thisTrial_2.color,edges=nVertices,units='height',size=[.5,.5])
    
    # keep track of which components have finished
    color_trialsComponents = [color_response, text_same]
    for thisComponent in color_trialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "color_trials"-------
    while continueRoutine:
        # get current time
        t = color_trialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *color_response* updates
        if t >= 0.0 and color_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            color_response.tStart = t
            color_response.frameNStart = frameN  # exact frame index
            color_response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(color_response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if color_response.status == STARTED:
            theseKeys = event.getKeys(keyList=['a', 'f'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                color_response.keys = theseKeys[-1]  # just the last key pressed
                color_response.rt = color_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # *text_same* updates
        if t >= 0.0 and text_same.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_same.tStart = t
            text_same.frameNStart = frameN  # exact frame index
            text_same.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in color_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "color_trials"-------
    for thisComponent in color_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if color_response.keys in ['', [], None]:  # No response was made
        color_response.keys=None
    trials_2.addData('color_response.keys',color_response.keys)
    if color_response.keys != None:  # we had a response
        trials_2.addData('color_response.rt', color_response.rt)
    if trials_2 > 0 and (trials_2.thisN +1) % 20 == 0:
        poly.setAutoDraw(False)
        win.flip()
        between_format_text.size = 0.8
        between_format_text.draw()
        win.flip()
        event.clearEvents()
        event.waitKeys(keyList=['d'])
    
    if trials_2.thisN == 0:
        correct = 1
    elif lastTrialColor == thisTrial_2.answer and color_response.keys in ['a']:
        correct = 1
    elif lastTrialColor != thisTrial_2.answer and color_response.keys in ['f']:
        correct = 1
    else:
        correct = 0
    
    lastTrialColor = thisTrial_2.answer
    
    lastnVertices = nVertices
    
    if trials_2.thisN % 2 == 1:
        trials_2.addData('colorpractice_correct',correct)
    
    trials_2.addData('colorpractice_numVertices',nVertices)
    
    poly.setAutoDraw(False)
    # the Routine "color_trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ISI_2"-------
    t = 0
    ISI_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if trials_2.thisN % 2 == 0:
        continueRoutine = False
    # keep track of which components have finished
    ISI_2Components = [fixation_2]
    for thisComponent in ISI_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISI_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_2* updates
        if t >= 0.0 and fixation_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_2.tStart = t
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_2.status == STARTED and t >= frameRemains:
            fixation_2.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI_2"-------
    for thisComponent in ISI_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 3.- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)





# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
