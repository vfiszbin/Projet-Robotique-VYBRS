from threading import Thread
from simulation.controller.controller import *
from SetStrategies import SetStrategies
from simulation import config
import sys

	

def main_simu():
	from simulation.modele.environment import Environment
	from simulation.viewer.view2D import View2D
	# from simulation.viewer.view3D import View3D
	from simulation.modele.updateModele import UpdateModele
	from SetEnvironment import SetEnvironment
	from simulation.modele.robot import Robot
	
	config.simu_or_real = 1 #var globale dans config, indique si le robot est simulé (1) ou réel (2)
	#Creation de l'environnement
	rob = Robot(400,150)
	env = Environment(800,300)
	SetE = SetEnvironment(env, rob)
	#Lance updateModele qui s'execute dans un thread secondaire
	update_modele = UpdateModele(env, rob)
	update_modele.start()
	#Creation des Strategies :
	SetS = SetStrategies(rob, env)
	#Lance le thread du controleur
	controller_thread = Thread(target=strategySequences, args=(SetS.sequences,))
	controller_thread.start()


	#Lance l'affichage graphique 2D ou 3D de la simulation qui s'execute sur le thread principal
	View2D(env)
	# View3D(env)



def main_real():
	from robot2I013 import Robot2I013 as Robot
	
	config.simu_or_real = 2 #var globale dans config, indique si le robot est simulé (1) ou réel (2)

	#Ajoute robot à l'environnement
	rob = Robot()
	#Preparation des Strategies
	SetS = SetStrategies(rob, None)

	#Lance le thread du controleur
	controller_thread = Thread(target=strategySequences, args=(SetS.sequences,))
	controller_thread.start()
	controller_thread.join()
	print("apreq join")


if __name__ == '__main__':
	if len(sys.argv) > 1 and sys.argv[1] == "-real": #le main_real s'execute si on passe l'arg -real en ligne de commande
		print(sys.argv[1])
		main_real()
	else: #sans argument spécifique, c'est le main_simu qui s'execute
		main_simu()
