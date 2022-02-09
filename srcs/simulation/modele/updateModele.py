from .obstacle import Obstacle
from time import sleep, time
from threading import Thread


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
		while(True):
			current_time = time()
			elapsed_time = current_time - self.last_time
			distance_covered = self.rob.speed * elapsed_time # Distance = Vitesse * Temps

			if distance_covered >= 0:
				self.rob.deplacerPositionRobotAvant(distance_covered)
			else :
				self.rob.deplacerPositionRobotArriere(-distance_covered)

			self.last_time = time()
			sleep(0.5)

