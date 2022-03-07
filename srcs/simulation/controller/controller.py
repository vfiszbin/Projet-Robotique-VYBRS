from time import sleep
from math import pi

UPDATE_FREQUENCY = 0.1 #en secondes

def TestStrategy(rob):

	sleep(2)
	
	launchStrategySeq(rob)
	print(rob.dir)

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

def launchStrategySeq(rob):
	stratSeq = StrategySeq(rob)
	s1 = TurnStrategy(rob, 90, 40)
	s2 = TurnStrategy(rob, -90, -50)
	s3 = TurnStrategy(rob, 360, 80)
	stratSeq.addStrategy(s1)
	stratSeq.addStrategy(s2)
	stratSeq.addStrategy(s3)
	while not stratSeq.stop():
		stratSeq.step()
		sleep(UPDATE_FREQUENCY)

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
			#reset l'angle dont ont tourné les roues avant de démarrer la prochaine stratégie
			self.rob.angle_rotated_left_wheel = 0
			self.rob.angle_rotated_right_wheel = 0
			self.sequence[self.current_strat].start()

		self.sequence[self.current_strat].step()

	def stop(self):
		return self.current_strat == len(self.sequence)-1 and self.sequence[self.current_strat].stop() #on a atteint la dernière strat et elle est terminée

class TraceASquare (StrategySeq) :
	def __init__(self, rob, length, speed,):
		super().__init__( rob)
		move = moveFowadStrategy(rob, length, speed)
		turnLeft = TurnStrategy(rob, rob.dir + 90, speed)
		self.sequence = [parcourir, tourner_droite] * 3 + [parcourir]


class moveFowardStrategy:
	"""
	class de strategie permet d'avancer le robot
	"""
	def __init__(self,rob,speed,distance):
		self.rob=rob
		self.distance_to_cover=distance
		self.distance_covered=0
		self.speed = speed
		self.angle_rotated_left_wheel = 0
		self.angle_rotated_right_wheel = 0

	def start(self):
		self.rob.changeWheelMode(1) #passe les roues en mode avancer
		self.rob.changeSpeed(abs(self.speed)) #donne une vitesse au robot pour commencer à avancer

	def step(self):
		#Récupère l'angle dont ont tourné les roues du robot depuis le début de la stratégie
		self.angle_rotated_left_wheel = self.rob.angle_rotated_left_wheel
		self.angle_rotated_right_wheel = self.rob.angle_rotated_right_wheel
		self.distance_covered += self.covered_distance()
		if self.stop():
			self.rob.changeSpeed(0)
			return

	def covered_distance(self):
		"""
		calcule la distance parcourue par le robot depuis last_time.
		"""
		distance = (2 * pi * self.radius_of_wheels) * (angle_rotated / 360) #distance parcourue à partir de l'angle effectué par les roues
		return distance

	def stop(self):
		return self.distance_covered >= self.distance_to_cover

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
		self.angle_rotated_left_wheel = 0
		self.angle_rotated_right_wheel = 0
		self.rob.changeWheelMode(2) #passe les roues en mode tourner
		self.rob.changeSpeed(self.speed) #donne une vitesse au robot pour commencer à tourner

	def step(self):
		#Récupère l'angle dont ont tourné les roues du robot depuis le début de la stratégie
		self.angle_rotated_left_wheel = self.rob.angle_rotated_left_wheel
		self.angle_rotated_right_wheel = self.rob.angle_rotated_right_wheel
		if self.stop():
			self.rob.changeSpeed(0) #arrête la rotation du robot
			return

	def stop(self):
		#Vérifie si les roues ont tourné de l'angle demandé
		if self.angle_to_rotate >= 0:
			return self.angle_rotated_left_wheel <= -(self.angle_to_rotate) and self.angle_rotated_right_wheel >= self.angle_to_rotate
		else:
			return self.angle_rotated_left_wheel >= -(self.angle_to_rotate) and self.angle_rotated_right_wheel <= self.angle_to_rotate

class TurnLeftStrategy(TurnStrategy):
	def __init__(self,rob,speed):
		super.__init__(rob,(rob.dir + 90),speed)
	def start(self):
		super.start()
	def step(self):
		super.step()
	def stop(self):
		super.stop()
