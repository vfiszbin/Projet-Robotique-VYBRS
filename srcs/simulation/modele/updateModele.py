from .obstacle import Obstacle
from time import sleep
from threading import Thread


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
		sleep(1)
		obs = Obstacle(83,116,20,25)
		self.env.addObject(obs)

		sleep(1)
		obs = Obstacle(116,32,58,56)
		self.env.addObject(obs)

		sleep(1)
		obs = Obstacle(200,100,30,40)
		self.env.addObject(obs)

		sleep(1)
		self.rob.deplacerPositionRobotAvant(10)

		sleep(1)
		self.rob.deplacerPositionRobotArriere(20)
