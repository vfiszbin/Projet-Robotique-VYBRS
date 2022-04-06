from time import sleep
from math import pi
from simulation import config

SAFE_DISTANCE = 300


UPDATE_FREQUENCY = 0.1 #en secondes


def strategySequences(sequences):

	for seq in sequences: #execute chaque séquence de stratégies de la liste sequences
		execStrategySeq(seq)
	print("fin stratseq")

def execStrategySeq(seq):
	#Execute la sequence de strategies
	while not seq.stop():
		seq.step()
		sleep(UPDATE_FREQUENCY)
	sleep(1) #pause dans la démo
	print("fin execstrat")

class StrategySeq :
	"""
	classe qui organise des séquences de strategie
	"""
	def __init__(self):
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

class moveForwardStrategy:
	"""
	Stratégie faisant avancer ou reculer un robot d'une certaine distance à une certaine vitesse
	"""
	def __init__(self,proxy,distance,speed):
		#Vitesse et distance_to_cover doivent avoir le même signe (aller dans la même direction)
		self.proxy = proxy
		self.distance_to_cover = distance
		self.distance_covered = 0
		self.speed = speed
		self.angle_rotated_left_wheel = 0
		self.angle_rotated_right_wheel = 0

	def start(self):
		#reset l'angle dont ont tourné les roues avant de démarrer la stratégie
		self.proxy.resetAngleRotated()
		self.proxy.setWheelMode(1) #passe les roues en mode avancer
		self.proxy.setSpeed(self.speed) #donne une vitesse au robot pour commencer à avancer/reculer

	def step(self):
		#Récupère l'angle dont ont tourné les roues du robot depuis le début de la stratégie
		self.angle_rotated_left_wheel = self.proxy.getAngleRotatedLeft()
		self.angle_rotated_right_wheel = self.proxy.getAngleRotatedRight()
		self.distance_covered = self.covered_distance()
		print("dst_covrd="+str(self.distance_covered))
		if self.stop():
			print("STOP ROBOT")
			self.proxy.setSpeed(0)
			return

	def covered_distance(self):
		"""
		calcule la distance parcourue par le robot selon l'angle dont les roues ont tourné
		"""
		distance = (2 * pi * self.proxy.getRadius() ) * (self.angle_rotated_left_wheel / 360) #distance parcourue à partir de l'angle effectué par les roues
		return distance

	def collision(self):
		"""
		rend True si le robot est proche d'un obstacle
		"""
		pas = self.proxy.getDistance()
		print("pas=" + str(pas))
		return pas <= SAFE_DISTANCE

	def stop(self):
		pas = self.proxy.getDistance()
		print("pas=" + str(pas))
		if pas <= SAFE_DISTANCE :
			print("pas <= safe")
			return True
		if self.distance_to_cover >= 0 :
			return self.distance_covered >= self.distance_to_cover
		else :
			return self.distance_covered <= self.distance_to_cover



class TurnStrategy:
	"""
	Stratégie faisant tourner un robot d'un certain angle à une certaine vitesse
	"""
	def __init__(self, proxy, angle, speed):
		#Vitesse et angle doivent avoir le même signe (aller dans la même direction)
		self.proxy = proxy
		self.speed = speed
		self.angle_to_rotate = angle
		self.angle_rotated_left_wheel = 0
		self.angle_rotated_right_wheel = 0
		self.angle_covered = 0

	def start(self):
		#reset l'angle dont ont tourné les roues avant de démarrer la stratégie
		self.proxy.resetAngleRotated()
		self.proxy.setWheelMode(2) #passe les roues en mode tourner
		self.proxy.setSpeed(self.speed) #donne une vitesse au robot pour commencer à tourner

	def step(self):
		#Récupère l'angle dont ont tourné les roues du robot depuis le début de la stratégie
		self.angle_rotated_left_wheel = self.proxy.getAngleRotatedLeft()
		self.angle_rotated_right_wheel = self.proxy.getAngleRotatedRight()
		print(self.angle_rotated_left_wheel)
		print(self.angle_rotated_right_wheel)
		self.angle_covered = self.covered_angle()
		if self.stop():
			self.proxy.setSpeed(0) #arrête la rotation du robot
			return

	def covered_angle(self):
		"""
		calcule l'angle dont a tourné par le robot depuis le début de la stratégie selon l'angle tourné par les roues
		"""
		distance = (2 * pi * self.proxy.getRadius() ) * (self.angle_rotated_right_wheel / 360) #distance parcourue à partir de l'angle effectué par les roues
		angle_covered = (360 * distance) / (2 * pi * self.proxy.getHalfDistBetweenWheels()) #angle dont le robot a tourné
		print("angle_covered=" + str(angle_covered))
		return angle_covered

	def stop(self):
		#Vérifie si les roues ont tourné de l'angle demandé
		if self.angle_to_rotate >= 0:
			return self.angle_covered >= self.angle_to_rotate
		else:
			return self.angle_covered <= self.angle_to_rotate

class moveBackwardStrategy(moveForwardStrategy):
	def __init__(self,proxy,speed,distance):
		super().__init__(proxy, -abs(speed), -abs(distance))



class SquareStrategy(StrategySeq) :
	""" classe qui organise une séquences de stratégie pour faire un parcours en forme de carré 
	"""
	def __init__(self, proxy, speed,length):
		super().__init__()
		move = moveForwardStrategy(proxy, speed, length )
		turnLeft = TurnStrategy(proxy, 90, speed / 2)
		self.sequence = [move, turnLeft] * 3 + [move]

class Navigate :
	""" classe qui permet d'alterner l'execution des deux stratégies 'moveForwardStrategy' et 'TurnStrategy' afin de naviger l'environment  sur une distance donner et tourner lorsque le robot s'approche d'un obstacle
	"""
	def __init__(self,proxy,speed,distance) :
		self.proxy=proxy
		self.speed=speed
		self.distance=distance
		self.move=moveForwardStrategy(proxy,speed,distance)
		self.turn=TurnStrategy(proxy,90,speed)
		self.running = None #pour savoir la stratégie en cours d'execution
		self.covered_distance = 0 

	def start(self) :
		self.running= self.move #on commence avec moveForwardStrategy
		self.move.start()

	def step(self) :
		if self.stop(): 
			self.proxy.setSpeed(0) #arrête le mouvement du robot
			return
		if self.running.stop() : #si la startegie courante s'arrete on bouscule vers la seconde
			if self.running == self.move : #si move s'arrete on lance turn
				#self.turn=TurnStrategy(self.rob,90,self.speed)
				self.running = self.turn
				self.turn.start()
			else :  # si turn s'arrete on réninitialise move et on la lance
				self.covered_distance = self.move.distance_covered 
				dist = self.distance -self.covered_distance # on recalcule la distance qui reste a faire
				self.move= moveForwardStrategy(self.proxy,self.speed,dist)
				self.running = self.move		
				self.running.start()
		self.running.step()	
			
	def stop(self) : 
		if self.move.distance_to_cover >= 0 :
			return self.move.distance_covered >= self.move.distance_to_cover
		else :
			return self.move.distance_covered <= self.move.distance_to_cover


class ArcStrategy:
	"""
	Stratégie faisant tracer au robot un arc de cercle d'un certain angle et d'un certain diametre
	"""
	def __init__(self, proxy, angle, speed, diameter):
		#Vitesse et angle doivent avoir le même signe (aller dans la même direction)
		self.proxy = proxy
		self.diameter = diameter #on considere que le diametre va du centre du cercle tracé par le robot à la roue intérieur (la plus proche du centre du cercle) du robot
		self.angle = angle
		self.speed = speed #vitesse de référence est celle de la roue intérieure
		self.angle_rotated_left_wheel = 0
		self.angle_rotated_right_wheel = 0
		self.covered_distance = 0

	def start(self):
		#reset l'angle dont ont tourné les roues avant de démarrer la stratégie
		self.proxy.resetAngleRotated()
		self.proxy.setWheelMode(3) #passe les roues en mode arc

		#Calcul de la vitesse et de la distance pour les roues
		r1 = self.diameter / 2 #rayon entre le centre du cercle décrit par le robot et la roue intérieure
		r2 = r1 + (self.proxy.getHalfDistBetweenWheels * 2) #rayon entre le centre du cercle décrit par le robot et la roue extérieure
		dg = (self.angle / 360) * 2 * pi * r1 #distance que la roue gauche doit parcourir
		dd = (self.angle / 360) * 2 * pi * r2 #distance que la roue droite doit parcourir
		ratio = dd / dg #ratio entre les distances

		self.distance_to_cover = dg #la roue intérieure sert de référence pour savoir si la stratégie est achevée

		#Le différentiel de vitesse entre les roues permet un trajectoire en arc de cercle
		self.proxy.setSpeedLeftWheel(self.speed) #vitesse de référence est celle de la roue intérieure
		self.proxy.setSpeedRightWheel(self.speed * ratio) #vitesse de la roue extérieure est ratio plus rapide


	def step(self):
		#Récupère l'angle dont ont tourné les roues du robot depuis le début de la stratégie
		self.angle_rotated_left_wheel = self.proxy.getAngleRotatedLeft()
		self.angle_rotated_right_wheel = self.proxy.getAngleRotatedRight()
		self.distance_covered = self.covered_distance()
		print("dst_covrd="+str(self.distance_covered))
		if self.stop():
			print("STOP ROBOT")
			self.proxy.setSpeed(0)
			return

	def covered_distance(self):
		"""
		calcule la distance parcourue par le robot selon l'angle dont les roues ont tourné
		"""
		distance = (2 * pi * self.proxy.getRadius() ) * (self.angle_rotated_left_wheel / 360) #distance parcourue à partir de l'angle effectué par la roue intérieure
		return distance

	def stop(self):
		pas = self.proxy.getDistance()
		print("pas=" + str(pas))
		if pas <= SAFE_DISTANCE :
			print("pas <= safe")
			return True
		if self.distance_to_cover >= 0 :
			return self.distance_covered >= self.distance_to_cover
		else :
			return self.distance_covered <= self.distance_to_cover
	