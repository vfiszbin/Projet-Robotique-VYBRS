from threading import Thread
from simulation.controller.controller import *
from SetStrategies import SetStrategies
from simulation import config
import sys
from simulation.modele.environment import Environment
from simulation.viewer.view2D import View2D
from simulation.modele.updateModele import UpdateModele
from SetEnvironment import SetEnvironment
from simulation.modele.robot import Robot


from simulation.controller.controller import *
from simulation.controller.proxy import ProxySimu, ProxyReal

def initializeProxy(rob, env):

	if config.simu_or_real == 1: #importe proxy simulation
		proxy = ProxySimu(rob, env)
		
	elif config.simu_or_real == 2: #importe proxy réel
		proxy = ProxyReal(rob)

	return proxy

def q1_1():
	###q1.1
	config.simu_or_real = 1 #var globale dans config, indique si le robot est simulé (1) ou réel (2)
	#Creation de l'environnement
	rob = Robot(300,200)
	env = Environment(800,300)
	SetE = SetEnvironment(env, rob)
	#Lance updateModele qui s'execute dans un thread secondaire
	update_modele = UpdateModele(env, rob)
	update_modele.start()
	
	#Lance l'affichage graphique 2D de la simulation qui s'execute sur le thread principal
	View2D(env)

def q2_1():
	config.simu_or_real = 1 #var globale dans config, indique si le robot est simulé (1) ou réel (2)
	#Creation de l'environnement
	rob = Robot(1000,500)
	env = Environment(2000,1000)
	SetE = SetEnvironment(env, rob)
	#Lance updateModele qui s'execute dans un thread secondaire
	update_modele = UpdateModele(env, rob)
	update_modele.start()

	#Creation des Strategies :
	proxy = initializeProxy(rob,env)
	#Prépare des séquences de stratégies que le controleur va executer
	sequences = [] #la liste contenant les séquences de stratégies
	seq=Motif1Strategy(proxy, 50)
	sequences.append(seq)

	#Lance le thread du controleur
	controller_thread = Thread(target=strategySequences, args=(sequences,))
	controller_thread.start()
	
	#Lance l'affichage graphique 2D de la simulation qui s'execute sur le thread principal
	View2D(env)

def q2_2():
	config.simu_or_real = 1 #var globale dans config, indique si le robot est simulé (1) ou réel (2)
	#Creation de l'environnement
	rob = Robot(1000,500)
	env = Environment(2000,1000)
	SetE = SetEnvironment(env, rob)
	#Lance updateModele qui s'execute dans un thread secondaire
	update_modele = UpdateModele(env, rob)
	update_modele.start()

	#Creation des Strategies :
	proxy = initializeProxy(rob,env)
	#Prépare des séquences de stratégies que le controleur va executer
	sequences = [] #la liste contenant les séquences de stratégies
	seq=Motif2Strategy(proxy, 100)
	sequences.append(seq)

	#Lance le thread du controleur
	controller_thread = Thread(target=strategySequences, args=(sequences,))
	controller_thread.start()
	
	#Lance l'affichage graphique 2D de la simulation qui s'execute sur le thread principal
	View2D(env)

def q2_3():
	config.simu_or_real = 1 #var globale dans config, indique si le robot est simulé (1) ou réel (2)
	#Creation de l'environnement
	rob = Robot(1000,500)
	env = Environment(2000,1000)
	SetE = SetEnvironment(env, rob)
	#Lance updateModele qui s'execute dans un thread secondaire
	update_modele = UpdateModele(env, rob)
	update_modele.start()

	#Creation des Strategies :
	proxy = initializeProxy(rob,env)
	#Prépare des séquences de stratégies que le controleur va executer
	sequences = [] #la liste contenant les séquences de stratégies
	seq=StrategySeq()
	s=RepeatMotif1Strategy(proxy, 100)
	seq.addStrategy(s)
	sequences.append(s)

	#Lance le thread du controleur
	controller_thread = Thread(target=strategySequences, args=(sequences,))
	controller_thread.start()
	
	#Lance l'affichage graphique 2D de la simulation qui s'execute sur le thread principal
	View2D(env)

q2_3()