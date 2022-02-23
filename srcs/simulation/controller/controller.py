from time import sleep

def TestStrategy(rob):
	sleep(2)
	rob.changeWheelMode(2)
	rob.changeSpeed(10)
	sleep(1)
	rob.changeSpeed(0)
	sleep(1)
	rob.changeSpeed(-10)
	sleep(1)
	rob.changeSpeed(0)
	sleep(1)
	rob.changeSpeed(30)
	sleep(1)
	rob.changeSpeed(0)

	sleep(1)
	rob.changeWheelMode(1)
	rob.changeSpeed(10)
	sleep(5)
	rob.changeSpeed(0)
	rob.changeWheelMode(2)
	rob.changeSpeed(-15)
	sleep(1)
	rob.changeWheelMode(1)
	rob.changeSpeed(50)
	sleep(3)
	rob.changeSpeed(0)
	rob.changeSpeed(-20)
	sleep(3)
	rob.changeSpeed(0)




class StrategySeq :
	"""
	classe qui organise des séquences de strategie
	"""
	def __init__(self):
		self.sequence=[]
	def addStrategy(self,strat):
		self.sequence.append(strat)
	def removeStrategy(self,strat):
		self.sequence.remove(strat)

class Strategy:
	"""
	classe qui Cree une nouvelle strategie
	"""
	def __init__(self):
		self.begin=False #chaque strategie a un debut et une fin
		self.end=False

class move(Strategy):
	"""
	class de strategie permet d'avancer le robot
	"""
	def __init__(self,rob,speed,distance):
		super().__init__()
		self.speed=speed
		self.rob=rob
		self.distance_to_cover=distance
		self.distance_covered=0
	def start(self):
		self.begin=True
		self.rob.changeSpeed(self.speed)
		#self.update_modele
	def stop(self):
		if self.distance_covered == self.distance :
			self.end=True
		else :
			print("fail")


class turn(Strategy):
	"""
	class de strategie: permet de tourner le robot	et l'avancer
	"""
	def __init__(self,rob,dir):
		super().__init__()
		self.dir=dir
		self.rob=rob
	def start(self):
		self.begin=True
		self.rob.changeDir(self.dir)
	def stop(self):
		if (rob.getDir()==self.dir) :
			self.end = True
		else :
			print("fail")
