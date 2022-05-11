from .controller import * 
from simulation import config
import keyboard
import time
from threading import Thread



def launchkeyevent(proxy,stratseqs):
	Dist_thread =Thread(target=readkeys,args=(proxy,stratseqs))
	Dist_thread.start()
	
def readkeys (proxy,stratseqs):
	events = keyboard.record('esc')
	if keyboard.read_key() == "up arrow":
		print(b)
		stratseqs.append(moveForwardStrategy(proxy,20,50))
	if keyboard.read_key() == "down arrow":
		stratseqs.append(moveForwardStrategy(proxy,20,-50))
	if keyboard.read_key() == "left arrow":
		stratseqs.append(TurnStrategy(proxy,5,20))
	if keyboard.read_key() == "right arrow":
		stratseqs.append(TurnStrategy(proxy,-5,20))
	sleep(2)
	#stratseqs.append(strat)
	

