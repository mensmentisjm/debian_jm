#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from psychopy import visual, core, event, gui #import some libraries from PsychoPy,
import random
import datetime
import csv
import os
from os import listdir
from os.path import isfile, join
#from os import path

mypath = '/home/jesmasta/downloads/bg/'
path_save_csv = '/home/jesmasta/downloads/psychopy_sample/'
path_get_csv = '/home/jesmasta/downloads/psychopy_sample/settings/output/csvs/'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]


#create a window
mywin = visual.Window([800,600],monitor="testMonitor", winType='pyglet', units="pix", fullscr = True)
#mywin = visual.Window([800,600],monitor="testMonitor", winType='pyglet', units="pix")
#mywin = visual.Window([800,600],monitor="testMonitor", units="deg", fullscr = True)
#mywin = visual.Window([1366,768], units="pix",winType='pygame')
#mywin = visual.Window([800,600], units="pix",winType='pygame', fullscr = True)
#mywin = visual.Window([800,600], units="pix",winType='pygame')

#ile razy pokazemy bodziec?
trials = 5

#exposal time
expo_time = 0.5
reaction_time_to_image = []

#Tekst powitalny i instrukcja
text_welcome=u"Witamy w eksperymencie! Za moment zobaczysz serie obrazkow. Po wyświetloym obrazku proszę wybrać jak najszybciej jedną pozycje z listy, która najbardziej pasuje do obrazka."
text_goodbye=u"Dziękujemy za udział w badaniu :). Nacisnij escape by wyjść."

#czasomierz whole exper
time_control = core.Clock()


#create some stimuli
#fixation = visual.PatchStim(win=mywin, size=0.2, pos=[0,0], sf=0, rgb=-1)
#fixation = visual.PatchStim(win=mywin, color=-1, colorSpace='rgb', tex=None, mask='circle',size=0.2)
fixation = visual.TextStim(mywin, text = "+", color='Black')


#tymczasowy identyfikator jest bieżącą chwilą czasową
tymczasowy=datetime.datetime.now().strftime("%d%m%Y%H%M")





####################
## ludi incipiant ##
####################
exp_time_begining = time_control.getTime()

welcome=visual.TextStim(mywin, text = text_welcome)
#welcome=visual.TextStim(mywin, text = words_string, wrapWidth =5)
welcome.draw()
mywin.flip()

while not 'space' in event.getKeys():
    #core.wait()
    pass

instrucitons_read = time_control.getTime()
instructions_time = instrucitons_read - exp_time_begining
#print("instructions_read ", instructions_read)   

#draw the stimuli and update the window
for i in range(trials):
    if len(onlyfiles) > 0:
        reaction_time_to_image.append(i)
        
        fixation.draw()
        mywin.flip()
        core.wait(1.0)
        
        # chooses random image form the folder
        choose = random.choice(onlyfiles)
        # removes the name of the file that was choosen
        onlyfiles.remove(choose)
        
        ### PRYMA OBRAZKOWA ###
        pryma = visual.ImageStim(win=mywin, image=mypath + choose, pos=(0,0))
        #########
        
        # we name our image and add it to the output list
        name = os.path.splitext(choose)[0]
        reaction_time_to_image.append(name)
        #print(name)
        
        ### creating list
        words_list = []

        with open(path_get_csv+name + '.csv', 'rb') as csvfile:
             spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
             for row in spamreader:
                 words_list.append(', '.join(row))
        
        proper_one = words_list[0]
        #print('proper_one: '+proper_one)
        #we have to remove the first, the proper element
        words_list.pop(0)
        #create string
        words_string = ' '.join(words_list)
        #convert into utf-8
        words_string  = unicode(words_string , "utf-8")
        ###########################
        
        # prepare slide with a list
        words_stim=visual.TextStim(mywin, text = words_string, wrapWidth =5)
        
        ### show background and a list ###
        pryma.draw()
        fixation.draw()
        mywin.flip()
        core.wait(expo_time)
        
        
        reaction_begin = time_control.getTime()
        
        words_stim.draw()
        mywin.flip()

        print(reaction_time_to_image)
        
        #waiting for a key to be pressed
        key_pressed=event.waitKeys(keyList=['1','2','3','4','5'])
        if ('1' in key_pressed): reaction_time_to_image.append(words_list[0])
        if ('2' in key_pressed): reaction_time_to_image.append(words_list[1])
        if ('3' in key_pressed): reaction_time_to_image.append(words_list[2])
        if ('4' in key_pressed): reaction_time_to_image.append(words_list[3])
        if ('5' in key_pressed): reaction_time_to_image.append(words_list[4])
        
        
        #print(words_list)
        if reaction_time_to_image[-1]==proper_one: reaction_time_to_image.append(1)
        else: reaction_time_to_image.append(0)
        
        
        # we get the reaction time
        reaction_end = time_control.getTime()
        reaction_time = reaction_end - reaction_begin
        reaction_time_to_image.append(reaction_time)
        
        
        
        if len(event.getKeys())>0: break
        event.clearEvents()





mywin.flip()
goodbye=visual.TextStim(mywin, text = text_goodbye)
goodbye.draw()
mywin.flip()

exp_time_ending = time_control.getTime()
exp_time = exp_time_ending - exp_time_begining 

while not 'escape' in event.getKeys():
    #core.wait()
    pass
        
goodbye_end = time_control.getTime()
goodbye_time = goodbye_end - exp_time_ending

mywin.close()

#dictionary
obiekt={'wiek':21,'plec':'F'}
boksik=gui.DlgFromDict(dictionary=obiekt, title='Dane')
if not (boksik.OK): 
    #AL lib: ReleaseALC: 1 device not closed
    core.quit()

metryczka=[]
metryczka.append(obiekt['plec'])
metryczka.append(obiekt['wiek'])
metryczka.append(tymczasowy)



pliczek=tymczasowy+".csv"
with open (path_save_csv + pliczek,'wb') as f:
    zapis=csv.writer(f)
    zapis.writerow(metryczka)
    zapis.writerow([expo_time])
    zapis.writerow([instructions_time, exp_time, goodbye_time])
    #zapis.writerow(reaction_time_to_image)
    for i in range(len(reaction_time_to_image)-1):
        if i%5 == 0 and i!=1:
            zapis.writerow([reaction_time_to_image[i], reaction_time_to_image[i+1], reaction_time_to_image[i+2], reaction_time_to_image[i+3], reaction_time_to_image[i+4]])
        
#	zapis.writerow(obroty)
#	zapis.writerow(czasy_reakcji)


#cleanup
core.quit()
########
