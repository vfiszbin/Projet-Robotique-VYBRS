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





class Strategy:
	"""
	classe qui Cree une nouvelle strategie
	"""
	def __init__(self):
		self.begin=False #chaque strategie a un debut et une fin
		self.end=False

	def start(self):
		"""
		methode qui commence une strategie
		"""
		self.begin=True
	def stop(self):
		"""
		methode qui termine la strategie
		"""
		self.end=True

class move(Strategy):
	"""
	class de strategie permet d'avancer le robot
	"""
	def __init__(self,rob,distance,speed):
		super().__init__()
		self.speed=speed
		self.distance=distance
		self.positionXB=rob.getPositionXRobot()
		self.positionYB=rob.getPositionYRobot()
		self.rob=rob
	def start(self):
		super().start()
		self.rob.changeSpeed(self.speed)
		self.rob.deplacerRobot(self.distance)

	def stop(self):
		if distance_covered(positionXB,positionYB,rob.getPositionXRobot(),rob.getPositionYRobot()) == self.distance :
			super().stop()
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
		super().start()
		self.rob.changeDir(self.dir)
	def stop(self):
		self.end = (rob.getDir()==self.dir)
