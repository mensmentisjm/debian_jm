#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from psychopy import visual, core, event, gui #import some libraries from PsychoPy,
import random
import datetime
import csv

#create a window
mywin = visual.Window([800,600],monitor="testMonitor", units="deg")
#mywin = visual.Window([800,600],monitor="testMonitor", units="deg", fullscr = True)
#mywin = visual.Window([1366,768], units="pix",winType='pygame')
#mywin = visual.Window([800,600], units="pix",winType='pygame')

#ile razy pokazemy bodziec?
trials = 2

#exposal time
#expo_time = 0.5

#Tekst powitalny i instrukcja
text_welcome="Witamy w eksperymencie! Za moment zobaczysz serie"
text_goodbye="Dziękujemy za udział w badaniu :). Nacisnij cokolwiek by wyjść."

#czasomierz whole exper
#time_control = core.Clock()

#czasomierz reaction
#rt_time = core.Clock()

#create some stimuli
#fixation = visual.PatchStim(win=mywin, size=0.2, pos=[0,0], sf=0, rgb=-1)
#fixation = visual.PatchStim(win=mywin, color=-1, colorSpace='rgb', tex=None, mask='circle',size=0.2)
fixation =visual.TextStim(mywin, text = "+", color='Black')
nyx = visual.ImageStim(win=mywin, image="illi.jpg", pos=(0,0))

#tymczasowy identyfikator jest bieżącą chwilą czasową
#tymczasowy=datetime.datetime.now().strftime("%d%m%Y%H%M")

#dictionary
#obiekt={'wiek':20,'plec':'F','kto':tymczasowy}
#boksik=gui.DlgFromDict(dictionary=obiekt, title='Dane')
#if not (boksik.OK): core.quit()

#metryczka=[]
#metryczka.append(obiekt['plec'])
#metryczka.append(obiekt['wiek'])
#metryczka.append(obiekt['kto'])



####################
##ludi incipiant ##
####################
#exp_time_begining = time_control.getTime()

welcome=visual.TextStim(mywin, text = text_welcome)
welcome.draw()
mywin.flip()

while not 'space' in event.getKeys():
    #core.wait()
    pass

#instrucitons_time = time_control.getTime()
#instructions_read = instrucitons_time - exp_time_begining
#print("instructions_read ", instructions_read)   

#draw the stimuli and update the window
for i in range(trials):
    if not 'escape' in event.getKeys():
        fixation.draw()
        mywin.flip()
        core.wait(1.0)
        
        nyx.draw()
        fixation.draw()
        mywin.flip()
        core.wait(0.5)
        
        
        #words.draw()
        #mywin.flip()
        #while not '1' in event.getKeys():
        
        
        if len(event.getKeys())>0: break
        event.clearEvents()






#pliczek=obiekt['kto']+".csv"
#with open (pliczek,'wb') as f:
#	zapis=csv.writer(f)
#	zapis.writerow(metryczka)
#	zapis.writerow(proby)
#	zapis.writerow(odpowiedzi)
#	zapis.writerow(obroty)
#	zapis.writerow(czasy_reakcji)


#cleanup
mywin.close()
core.quit()
