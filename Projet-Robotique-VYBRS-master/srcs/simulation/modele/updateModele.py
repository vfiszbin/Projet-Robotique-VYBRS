from .. import config
from time import sleep
from threading import Thread

UPDATE_FREQUENCY = 0.1 #en secondes

class UpdateModele(Thread):
	def __init__(self, env, rob):
		super(UpdateModele, self).__init__()
		self.env = env
		self.rob = rob

	def run(self):
		'''
		Cette fonction regroupe les instructions de mise à jour de la partie modèle de la simulation.
		Cette fonction s'execute dans un thread secondaire.
		'''
		while(config.run):
			self.rob.update() #Maj la position ou la direction du robot
			sleep(UPDATE_FREQUENCY)
