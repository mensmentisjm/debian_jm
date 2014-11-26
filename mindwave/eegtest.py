from psychopy import visual, core, event
from pymindwave.parser import Parser
import random
import pickle
import datetime
terrraz=datetime.datetime.now().strftime('%d%m%Y%H%M')
print(terrraz)

zegarek=core.Clock()

cyfry=range(10)
napisy=['zero','jeden','dwa','trzy','cztery','piec','szesc','siedem','osiem','dziewiec']
napisy_set=set(napisy)
typy_triali=[]
triale_napisy=[]
triale_cyfry=[]
szansa_spojnego=0.85
#core.checkPygletDuringWait = False
typy_triali=[]
ile_triali=50

for i in range(ile_triali):
	triale_cyfry.append(random.choice(cyfry))
	if random.random()<szansa_spojnego:
		typy_triali.append('spojny')
		triale_napisy.append(napisy[triale_cyfry[-1]])
	else:
		typy_triali.append('niespojny')
		zbior_zubozony=napisy_set-set([napisy[triale_cyfry[-1]]])
		triale_napisy.append(zbior_zubozony.pop())
		

p = Parser('/dev/rfcomm0')

okienko=visual.Window(units='pix',winType='pygame',fullscr=True)
intro=visual.TextStim(win=okienko,text='Nastepna cyfra to...',color='black',height=50,pos=(0,100))
napis=visual.TextStim(win=okienko,color='black',height=50,pos=(0,-100))
cyfra=visual.TextStim(win=okienko,color='black',height=100,pos=(0,0))

dobrze=visual.TextStim(win=okienko,text=': )',color='green',height=100,pos=(0,0))
zle=visual.TextStim(win=okienko,color='red',text= ': <',height=100,pos=(0,0))

odczyty=[]
odpowiedzi=[]
okienko.setMouseVisible(False)
for i in range(ile_triali):
	levele=[]
	wektory=[]
	atencje=[]
	medytacje=[]
	blinki=[]
	jakosci=[]
	napis.setText(triale_napisy[i])
	cyfra.setText(str(triale_cyfry[i]))
	intro.draw()
	napis.draw()
	okienko.flip()
	core.wait(0.5)
	
	okienko.flip
	core.wait(0.5)
	
	cyfra.draw()
	okienko.flip()
	czas=zegarek.getTime()
	while ((zegarek.getTime()-czas)<1):
		p.update()
		levele.append(p.raw_values[-1])
		wektory.append(p.current_vector)
		atencje.append(p.current_attention)
		medytacje.append(p.current_meditation)
		blinki.append(p.current_blink_strength)
		try:
			jakosci.append(p.poor_signal)
		except AttributeError:
			jakosci.append(666)
		core.wait(0.01)
	reakcja=event.waitKeys(keyList=['z','m'])
	if (typy_triali[i]=='spojny'):
		if 'z' in reakcja: odpowiedzi.append("ok")
		else: odpowiedzi.append("zle")
	else:
		if 'z' in reakcja: odpowiedzi.append("zle")
		else: odpowiedzi.append("ok")
		
	if (odpowiedzi[-1]=="ok"): dobrze.draw()
	else: zle.draw()
	okienko.flip()
	core.wait(0.5)
	
	odczyt=[levele,wektory,atencje,medytacje,blinki,jakosci]
	odczyty.append(odczyt)
	okienko.flip()
	core.wait(0.5)

do_zapisu=[typy_triali,odpowiedzi,odczyty]
pickle.dump(do_zapisu, open( terrraz+'.pikiel', 'wb' ))
okienko.close()
core.quit()