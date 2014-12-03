#!/usr/bin/env python

from psychopy import visual, core, event
from parser import Parser
import random
import pickle
import datetime


p = Parser()



for i in range(5):
    levele=[]
    wektory=[]
    atencje=[]
    medytacje=[]
    blinki=[]
    jakosci=[]
    core.wait(0.5)

    p.update()
    levele.append(p.raw_values[0])
    wektory.append(p.current_vector)
    atencje.append(p.current_attention)
    medytacje.append(p.current_meditation)
#    blinki.append(p.current_blink_strength)
    try:
        jakosci.append(p.poor_signal)
    except AttributeError:
        jakosci.append(666)
    core.wait(0.5)

print("levele " + str(levele))
print("wektory" + str(wektory))
print("arencje" + str(atencje))
print("medytacje" + str(medytacje))
print("blinki" + str(blinki))
print("jakosci" + str(jakosci))
