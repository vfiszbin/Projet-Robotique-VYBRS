
from simulation.modele.environment import Environment
from simulation.modele.obstacle import Obstacle, Wall
from simulation.modele.robot import Robot
from simulation.viewer.view2D import View2D
from simulation.modele.updateModele import UpdateModele
from threading import Thread
from simulation.controller.controller import *
from simulation import config
import sys


def main_simu():
	config.simu_or_real = 1 #var globale dans config, indique si le robot est simulé (1) ou réel (2)

	#Creation de l'environnement
	env = Environment(800,300)

	#Tests robot
	rob = Robot(300,240)
	env.addRob(rob)
	print(env.objects)
	print("dir=" + str(rob.dir))
	print("posX=" + str(rob.positionX))
	print("posY=" + str(rob.positionY))


	#Tests obstacle
	obs = Obstacle(10,50,100,30)
	env.addObs(obs)
	print(env.objects)
	obs2 = Obstacle(600,180,30,100)
	env.addObs(obs2)
	print(env.objects)



	# Ajout d'un mur
	mur=Wall(0,0,env.height,90)
	mur2=Wall(env.width-5,0,env.height,90)
	mur3=Wall(6,0,env.width-12,0)
	mur4=Wall(6,env.height-5,env.width-12,0)
	env.addObs(mur)
	env.addObs(mur2)
	env.addObs(mur3)
	env.addObs(mur4)

	#Lance updateModele qui s'execute dans un thread secondaire
	update_modele = UpdateModele(env,rob)
	update_modele.start()


	#Lance le thread du controleur
	controller_thread = Thread(target=TestStrategy, args=(rob,))
	controller_thread.start()

	#Lance l'affichage graphique 2D de la simulation qui s'execute sur le thread principal
	View2D(env)

def main_real():
	config.simu_or_real = 2 #var globale dans config, indique si le robot est simulé (1) ou réel (2)

	#Creation de l'environnement
	env = Environment(800,300)

	#Ajoute robot à l'environnement
	rob = Robot(300,240)
	env.addRob(rob)

	#Lance updateModele qui s'execute dans un thread secondaire
	update_modele = UpdateModele(env,rob)
	update_modele.start()

	#Lance le thread du controleur
	controller_thread = Thread(target=TestStrategy, args=(rob,))
	controller_thread.start()

	#Lance l'affichage graphique 2D de la simulation qui s'execute sur le thread principal
	View2D(env)


if __name__ == '__main__':
	if len(sys.argv) > 1 and sys.argv[1] == "-real":
		print(sys.argv[1])
		main_real()
	else:
		main_simu()
