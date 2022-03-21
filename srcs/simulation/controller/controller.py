from time import sleep
from math import pi
from simulation import config
from .proxy import ProxySimu, ProxyReal


def importProxy(rob):
	global Proxy #proxy déclaré en global pour y avoir accès partout dans le controleur
	if config.simu_or_real == 1: #importe proxy simulation
		Proxy = ProxySimu(rob)
		
	elif config.simu_or_real == 2: #importe proxy réel
		Proxy = ProxyReal(rob)



UPDATE_FREQUENCY = 0.01 #en secondes

def TestStrategy(rob):
	print("dir=" + str(rob.dir))
	print("posX=" + str(rob.positionX))
	print("posY=" + str(rob.positionY))

	# rob.changeWheelMode(2)
	# rob.changeSpeed(100)
	# sleep(1)
	# rob.changeSpeed(0)
	# sleep(1)
	# rob.changeSpeed(-120)
	# sleep(1)
	# rob.changeSpeed(0)
	# sleep(1)
	# rob.changeSpeed(380)
	# sleep(1)
	# rob.changeSpeed(0)

	# rob.changeWheelMode(1)
	# rob.changeSpeed(360)
	# sleep(5)
	# rob.changeSpeed(0)
	# rob.changeWheelMode(2)
	# rob.changeSpeed(-260)
	# sleep(1)
	# rob.changeWheelMode(1)
	# rob.changeSpeed(360)
	# sleep(3)
	# rob.changeSpeed(0)
	# rob.changeSpeed(-180)
	# sleep(3)
	# rob.changeSpeed(0)

def strategySequences(rob, sequences):

	importProxy(rob)

	for seq in sequences: #execute chaque séquence de stratégies de la liste sequences
		execStrategySeq(seq)

def execStrategySeq(seq):
	#Execute la sequence de strategies
	while not seq.stop():
		seq.step()
		sleep(UPDATE_FREQUENCY)
	sleep(1) #pause dans la démo

class StrategySeq :
	"""
	classe qui organise des séquences de strategie
	"""
	def __init__(self, rob):
		self.rob = rob
		self.sequence=[]
		self.current_strat = -1

	def addStrategy(self, strat):
		self.sequence.append(strat)

	def removeStrategy(self, strat):
		self.sequence.remove(strat)

	def step(self):
		if self.stop(): #toutes les strat de la seq ont été executées
			return

		if self.current_strat < 0 or self.sequence[self.current_strat].stop(): #démarrage de la prochaine strat
			self.current_strat += 1
			self.sequence[self.current_strat].start()

		self.sequence[self.current_strat].step()

	def stop(self):
		return self.current_strat == len(self.sequence)-1 and self.sequence[self.current_strat].stop() #on a atteint la dernière strat et elle est terminée

class SquareStrategy(StrategySeq) :
	""" classe qui organise une séquences de stratégie pour faire un parcours en forme de carré 
	"""
	def __init__(self, rob, speed,length):
		super().__init__(rob)
		move = moveForwardStrategy(rob , speed, length )
		turnLeft = TurnStrategy(rob, 90, speed/2)
		self.sequence = [move, turnLeft] * 3 + [move]


class moveToPositionXY(StrategySeq) :
	"""classe qui organise une séquences de stratégie pour faire un deplacement vers un point
	"""
	def __init__(self,rob,speed,X,Y) :
		super().__init__(rob)
		robx = self.positionX
		roby = self.positionY
		dir = self.dir * pi / 180
		dx =  robx * cos(dir) + roby * sin(dir)
		dy = robx * sin(dir) + roby * cos(dir)


class moveForwardStrategy:
	"""
	Stratégie faisant avancer ou reculer un robot d'une certaine distance à une certaine vitesse
	"""
	def __init__(self,rob,speed,distance):
		#Vitesse et distance_to_cover doivent avoir le même signe (aller dans la même direction)
		self.rob = rob
		self.distance_to_cover = distance
		self.distance_covered = 0
		self.speed = speed
		self.angle_rotated_left_wheel = 0
		self.angle_rotated_right_wheel = 0

	def start(self):
		#reset l'angle dont ont tourné les roues avant de démarrer la stratégie
		Proxy.resetAngleRotated()
		self.rob.changeWheelMode(1) #passe les roues en mode avancer
		self.rob.setSpeed(self.speed) #donne une vitesse au robot pour commencer à avancer/reculer

	def step(self):
		#Récupère l'angle dont ont tourné les roues du robot depuis le début de la stratégie
		self.angle_rotated_left_wheel = Proxy.getAngleRotatedLeft()
		self.angle_rotated_right_wheel = Proxy.getAngleRotatedRight()
		self.distance_covered = self.covered_distance()
		if self.stop():
			self.rob.setSpeed(0)
			return

	def covered_distance(self):
		"""
		calcule la distance parcourue par le robot selon l'angle dont les roues ont tourné
		"""
		distance = (2 * pi * self.rob.radius_of_wheels) * (self.angle_rotated_left_wheel / 360) #distance parcourue à partir de l'angle effectué par les roues
		return distance

	def collision(self):
		"""
		rend True si le robot est proche d'un obstacle
		"""
		self.rob.getDistance() <= safe_distance

	def stop(self):
		if self.distance_to_cover >= 0 :
			return self.distance_covered >= self.distance_to_cover and self.collision()
		else :
			return self.distance_covered <= self.distance_to_cover



class TurnStrategy:
	"""
	Stratégie faisant tourner un robot d'un certain angle à une certaine vitesse
	"""
	def __init__(self, rob, angle, speed):
		#Vitesse et angle doivent avoir le même signe (aller dans la même direction)
		self.rob = rob
		self.speed = speed
		self.angle_to_rotate = angle
		self.angle_rotated_left_wheel = 0
		self.angle_rotated_right_wheel = 0

	def start(self):
		#reset l'angle dont ont tourné les roues avant de démarrer la stratégie
		Proxy.resetAngleRotated()
		self.rob.changeWheelMode(2) #passe les roues en mode tourner
		self.rob.setSpeed(self.speed) #donne une vitesse au robot pour commencer à tourner

	def step(self):
		#Récupère l'angle dont ont tourné les roues du robot depuis le début de la stratégie
		self.angle_rotated_left_wheel = Proxy.getAngleRotatedLeft()
		self.angle_rotated_right_wheel = Proxy.getAngleRotatedRight()
		if self.stop():
			self.rob.setSpeed(0) #arrête la rotation du robot
			return

	def stop(self):
		#Vérifie si les roues ont tourné de l'angle demandé
		if self.angle_to_rotate >= 0:
			return self.angle_rotated_left_wheel <= -(self.angle_to_rotate) and self.angle_rotated_right_wheel >= self.angle_to_rotate
		else:
			return self.angle_rotated_left_wheel >= -(self.angle_to_rotate) and self.angle_rotated_right_wheel <= self.angle_to_rotate

class moveBackwardStrategy(moveForwardStrategy):
	def __init__(self,rob,speed,distance):
		super().__init__(rob, -abs(speed), -abs(distance))

	
