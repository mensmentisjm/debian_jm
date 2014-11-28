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

experimental_group = 1 
preparation  = 1
expo_time = 0.1

if experimental_group == 1:
    path_get_image = 'ppk_perc_materials/experimental_group/'
    path_save_csv = 'csv_output/'
else:
    path_get_image = 'ppk_perc_materials/control_group/'
    path_save_csv = 'csv_output_control/'


path_get_image_test = 'ppk_perc_materials/series_test/'
path_get_csv = 'ppk_perc_materials/csv/'

onlyfiles = [ f for f in listdir(path_get_image) if isfile(join(path_get_image,f)) ]
test_names = [ f for f in listdir(path_get_image_test) if isfile(join(path_get_image_test,f)) ]

#fixation_size
fix_size = 30
# font size
font_size = 30

#ile razy pokazemy bodziec?
trials = 18
#ile obrazkow pokazujemy na probe
ile_preperation = 3
ile_main = trials - ile_preperation

# times
reaction_time_to_image = []
reactions_time_preparation = 0
reactions_time_main = 0

#Tekst powitalny i instrukcja
text_welcome=u"Witamy w eksperymencie! Za moment zobaczysz serie obrazków. Przed wyświetleniem każdego obrazka pojawi się punkt fiksacji (krzyżyk). Skup na nim wzrok. Po wyświetlonym obrazku wybierz proszę jak najszybciej jedną pozycje z listy wyrazów (naciskając odpowiednio 1, 2, 3, 4 lub 5). Naciśnij spację by przejść dalej."
text_preparation_begin=u"Pierwsze kilka obrazków zostanie zaprezentowane na próbę. Naciśnij spację by rozpocząć serię próbną."
text_preparation_end=u"Teraz możemy przejść do głównego badania. Naciśnij spację by rozpocząć właściwą część eksperymentu."
text_goodbye=u"Dziękujemy za udział w badaniu. :) Nacisnij escape by wyjść."


##############################################
#create a window  ,fullscr = True
mywin = visual.Window([2560, 1440],monitor="testMonitor", winType='pyglet', units="pix", fullscr = True, )
mywin.setMouseVisible(False)

win_end = visual.Window([1500,800],monitor="testMonitor", winType='pyglet', units="pix")


#mywin = visual.Window([800,600],monitor="testMonitor", winType='pyglet', units="pix")
#mywin = visual.Window([800,600],monitor="testMonitor", units="deg", fullscr = True)
#mywin = visual.Window([1366,768], units="pix",winType='pygame')
#mywin = visual.Window([800,600], units="pix",winType='pygame', fullscr = True)
#mywin = visual.Window([800,600], units="pix",winType='pygame')


#czasomierz whole exper
time_control = core.Clock()


#create some stimuli
#fixation = visual.PatchStim(win=mywin, size=0.2, pos=[0,0], sf=0, rgb=-1)
#fixation = visual.PatchStim(win=mywin, color=-1, colorSpace='rgb', tex=None, mask='circle',size=0.2)
fixation = visual.TextStim(mywin, text = "+", color='Black', height=fix_size)


#tymczasowy identyfikator jest bieżącą chwilą czasową
tymczasowy=datetime.datetime.now().strftime("%Y%m%d%H%M")


####################
## ludi incipiant ##
####################
experiment_time_begining = time_control.getTime()

welcome=visual.TextStim(mywin, text = text_welcome, height=font_size)
#welcome=visual.TextStim(mywin, text = words_string, wrapWidth =5)
welcome.draw()
mywin.flip()

while not 'space' in event.getKeys():
    #core.wait()
    pass

instrucitons_read = time_control.getTime()
instructions_time = instrucitons_read - experiment_time_begining
#print("instructions_read ", instructions_read)

if preparation == 1:
    preparation_begin=visual.TextStim(mywin, text = text_preparation_begin, height=font_size)
    preparation_begin.draw()
    mywin.flip()
    while not 'space' in event.getKeys():
        #core.wait()
        pass
    instructions_read_prep_begin = time_control.getTime()
    instructions_time_prep_begin = instructions_read_prep_begin - instrucitons_read
else:
    instructions_time_prep_begin = 0


#draw the stimuli and update the window
for i in range(trials):
    if len(onlyfiles) > 0:

        if preparation == 1 and i == ile_preperation:
            preparation_end=visual.TextStim(mywin, text = text_preparation_end, height=font_size)
            preparation_end.draw()
            mywin.flip()
            instructions_read_prep_end_start = time_control.getTime()
            while not 'space' in event.getKeys():
                #core.wait()
                pass
            instructions_read_prep_end_stop = time_control.getTime()
            instructions_time_prep_end = instructions_read_prep_end_stop - instructions_read_prep_end_start
        if preparation == 0:
            instructions_time_prep_end = 0

        reaction_time_to_image.append(i+1)

        fixation.draw()
        mywin.flip()
        core.wait(1.0)

        # chooses random image form the folder

        if preparation == 1 and len(test_names)>0:
            choose = random.choice(test_names)
            # removes the name of the file that was choosen
            test_names.remove(choose)
        else:
            choose = random.choice(onlyfiles)
            # removes the name of the file that was choosen
            onlyfiles.remove(choose)

        #print(len(test_names))

        ### PRYMA OBRAZKOWA ###
        if preparation == 1 and i<ile_preperation:
            #print('weszlo')
            pryma = visual.ImageStim(win=mywin, image=path_get_image_test + choose, pos=(0,0))
        else:
            pryma = visual.ImageStim(win=mywin, image=path_get_image + choose, pos=(0,0))
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
        words_stim=visual.TextStim(mywin, text = words_string, wrapWidth =5, height=font_size)

        ### show background and a list ###
        pryma.draw()
        fixation.draw()
        mywin.flip()
        core.wait(expo_time)


        reaction_begin = time_control.getTime()

        words_stim.draw()
        mywin.flip()


        #waiting for a key to be pressed
        key_pressed=event.waitKeys(keyList=['1','2','3','4','5','delete'])
        if ('1' in key_pressed):
            reaction_time_to_image.append(words_list[0])
        if ('2' in key_pressed):
            reaction_time_to_image.append(words_list[1])
        if ('3' in key_pressed):
            reaction_time_to_image.append(words_list[2])
        if ('4' in key_pressed):
            reaction_time_to_image.append(words_list[3])
        if ('5' in key_pressed):
            reaction_time_to_image.append(words_list[4])
        if ('delete' in key_pressed):
            break


        if preparation == 1 and i<ile_preperation:
            reaction_time_to_image[-1] = "test"

        #print(words_list)
        if reaction_time_to_image[-1]==proper_one: reaction_time_to_image.append(1)
        else: reaction_time_to_image.append(0)


        # we get the reaction time
        reaction_end = time_control.getTime()
        reaction_time = reaction_end - reaction_begin
        reaction_time_to_image.append(reaction_time)

        if preparation == 1:
            if i < ile_preperation:
                reactions_time_preparation += reaction_time
            else:
                reactions_time_main += reaction_time
        else:
            reactions_time_preparation = 0
            reactions_time_main += reaction_time










mywin.flip()
goodbye=visual.TextStim(mywin, text = text_goodbye, height=font_size)
goodbye.draw()
mywin.flip()


goodbye_end_start = time_control.getTime()
while not 'escape' in event.getKeys():
    #core.wait()
    pass

goodbye_end_stop = time_control.getTime()
goodbye_time = goodbye_end_stop - goodbye_end_start

mywin.close()

#time of the entire experiment
experiment_entire_stops = time_control.getTime()
experiment_entire_time = experiment_entire_stops - experiment_time_begining

win_end.flip()


#dictionary
obiekt={'kierunek(p=psycho/c=cogni/i=inny/n=nie studiuje)':'c','wiek':21,'plec(k/m)':'k'}
boksik=gui.DlgFromDict(dictionary=obiekt, title='Dane')
if not (boksik.OK):
    #AL lib: ReleaseALC: 1 device not closed
    core.quit()

metryczka=[]
metryczka.append(obiekt['plec(k/m)'])
metryczka.append(obiekt['wiek'])
metryczka.append(obiekt['kierunek(p=psycho/c=cogni/i=inny/n=nie studiuje)'])
metryczka.append(tymczasowy)

win_end.close()

pliczek=tymczasowy+".csv"
with open (path_save_csv + pliczek,'wb') as f:
    zapis=csv.writer(f)
    zapis.writerow(metryczka)
    zapis.writerow([experimental_group,expo_time, ile_preperation,ile_main,trials])
    zapis.writerow([instructions_time, instructions_time_prep_begin, instructions_time_prep_end, goodbye_time, experiment_entire_time])
    zapis.writerow([reactions_time_preparation, reactions_time_main])
    #zapis.writerow(reaction_time_to_image)
    for i in range(len(reaction_time_to_image)-1):
        if i%5 == 0 and i!=1:
            zapis.writerow([reaction_time_to_image[i], reaction_time_to_image[i+1], reaction_time_to_image[i+2], reaction_time_to_image[i+3], reaction_time_to_image[i+4]])

#	zapis.writerow(obroty)
#	zapis.writerow(czasy_reakcji)


#cleanup
core.quit()
########
