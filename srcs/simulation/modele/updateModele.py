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

			self.rob.update(distance_covered) #Maj la position ou la direction du robot selon la distance parcourue et le wheelMode du robot

			self.last_time = time()
			sleep(UPDATE_FREQUENCY)
