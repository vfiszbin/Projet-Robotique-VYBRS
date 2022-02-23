from .obstacle import Obstacle
from .. import config
from time import sleep, time
from threading import Thread
from random import *

UPDATE_FREQUENCY = 0.1 #en secondes

class UpdateModele(Thread):
	def __init__(self, env, rob):
		super(UpdateModele, self).__init__()
		self.env = env
		self.rob = rob
		self.last_time = time()

	def run(self):
		'''
		Cette fonction regroupe les instructions de mise à jour de la partie modèle de la simulation.
		Cette fonction s'execute dans un thread secondaire.
		'''
		while(config.run):
			current_time = time()
			elapsed_time = current_time - self.last_time
			distance_covered = self.rob.speed * elapsed_time # Distance = Vitesse * Temps

			if self.rob.wheelMode == 1: #roues en mode 1 pour avancer/reculer
<<<<<<< HEAD
				if distance_covered >= 0:
					self.rob.deplacerRobot(distance_covered)
				else :
					self.rob.deplacerRobot(-distance_covered)
=======
				self.rob.deplacerRobot(distance_covered)
>>>>>>> 8712267b824e3107ac241da9760ee869f08a082d
			elif self.rob.wheelMode == 2: #roues en mode 2 pour tourner
				self.rob.updateDir(distance_covered)

			self.last_time = time()
			sleep(UPDATE_FREQUENCY)
