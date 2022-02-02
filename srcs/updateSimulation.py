from obstacle import Obstacle
from time import sleep

def updateSimulation(env,rob):
	'''
	Cette fonction regroupe les instructions de mise à jour de la simulation en temps réel.
	Si l'affichage graphique a été démarré, cette fonction s'execute dans un thread secondaire
	et ses instructions sont les seules à pouvoir s'executer, le main thread étant occupé par l'affichage graphique
	'''
	# sleep(1)
	# obs = obstacle(83,116,20,25)
	# env.addObject(obs)

	# sleep(1)
	# obs = obstacle(116,32,58,56)
	# env.addObject(obs)

	# sleep(1)
	# obs = obstacle(200,100,30,40)
	# env.addObject(obs)

	# changer la direction du robot
	sleep(2)
	rob.deplacerPositionRobotAvant(10,30,20)
	sleep(2)
	rob.deplacerPositionRobotArriere(20,20,10)

	# deplace la direction du robot au coordonnes voulue
	#rob.deplacerRobotVersPosition(5,-3,47,50)
