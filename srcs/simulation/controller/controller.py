from time import sleep
from math import pi
from simulation import config
from threading import Thread

SAFE_DISTANCE = 50 #bonne valeur pour le vrai robot = 300 mm


UPDATE_FREQUENCY = 0.1 #en secondes

def updateLatestDist(proxy):

	while not config.Fin_Strat :
		# print("fin strat",config.Fin_Strat)
		sleep(1)
		config.Latest_Dist=proxy.getDistance()  #initialisé à 100 dans config.py
		# print("la get distance",config.Latest_Dist)

def launchThreadDist(proxy):

	Dist_thread =Thread(target=updateLatestDist,args=(proxy,))
	Dist_thread.start()
	

def strategySequences(sequences):

	for seq in sequences: #execute chaque séquence de stratégies de la liste sequences
		execStrategySeq(seq)
	print("fin stratseq")
	config.Fin_Strat = True
	print("in StratSeq ",config.Fin_Strat)

def execStrategySeq(seq):
	#Execute la sequence de strategies
	while not seq.stop():
		seq.step()
		sleep(UPDATE_FREQUENCY)
	# sleep(1) #pause dans la démo

class StrategySeq :
	"""
	classe qui organise des séquences de strategie
	"""
	def __init__(self,proxy):
		self.sequence=[]
		self.current_strat = -1
		launchThreadDist(proxy)

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

		if self.stop():
			self.proxy.setSpeed(0)
			return

	def covered_distance(self):
		"""
		calcule la distance parcourue par le robot selon l'angle dont les roues ont tourné
		"""
		distance = (2 * pi * self.proxy.getRadius() ) * (self.angle_rotated_left_wheel / 360) #distance parcourue à partir de l'angle effectué par les roues
		return distance

	def stop(self):
		pas = config.Latest_Dist
		# print("pas=" + str(pas))
		if pas <= SAFE_DISTANCE :
			config.obstacle_ahead = True
			self.proxy.setSpeed(0)
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
	Si to_left_or_right == 0 : le robot trace un arc de cercle à sa gauche
	Vitesse et angle positifs : le robot trace un arc de cercle dans le sens anti horaire en roulant vers l'avant
	Vitesse et angle négatifs : le robot trace un arc de cercle dans le sens horaire en roulant en reculant
	Si to_left_or_right == 1 : le robot trace un arc de cercle à sa droite
	C'est l'inverse
	"""
	def __init__(self, proxy, angle, speed, diameter, to_left_or_right):

		self.proxy = proxy
		self.diameter = diameter #on considere que le diametre va du centre du cercle tracé par le robot à la roue intérieur (la plus proche du centre du cercle) du robot
		self.angle = angle
		self.speed = speed #vitesse de référence est celle de la roue intérieure
		self.angle_rotated_left_wheel = 0
		self.angle_rotated_right_wheel = 0
		self.distance_covered = 0
		self.to_left_or_right = to_left_or_right

	def start(self):
		#reset l'angle dont ont tourné les roues avant de démarrer la stratégie
		self.proxy.resetAngleRotated()
		self.proxy.setWheelMode(3) #passe les roues en mode arc

		#Calcul de la vitesse et de la distance pour les roues
		r1 = self.diameter / 2 #rayon entre le centre du cercle décrit par le robot et la roue intérieure
		r2 = r1 + (self.proxy.getHalfDistBetweenWheels() * 2) #rayon entre le centre du cercle décrit par le robot et la roue extérieure

		#on veut decrire un arc de cercle a gauche du robot
		if (self.to_left_or_right == 0): 
			dg = (self.angle / 360) * 2 * pi * r1 #distance que la roue gauche doit parcourir
			dd = (self.angle / 360) * 2 * pi * r2 #distance que la roue droite doit parcourir

			ratio = dg / dd #ratio entre les distances

			self.distance_to_cover = dg #la roue gauche sert de référence pour savoir si la stratégie est achevée

			#Le différentiel de vitesse entre les roues permet un trajectoire en arc de cercle
			self.proxy.setSpeedLeftWheel(self.speed * ratio) #vitesse de la roue intérieure est ratio moins rapide que celle de la roue exterieure
			self.proxy.setSpeedRightWheel(self.speed)

		#on veut decrire un arc de cercle a droite du robot
		else : 
			#inverse dd et dg
			dd = (self.angle / 360) * 2 * pi * r1
			dg = (self.angle / 360) * 2 * pi * r2

			ratio = dd / dg #ratio entre les distances inversé
			self.distance_to_cover = dg

			self.proxy.setSpeedLeftWheel(self.speed)
			self.proxy.setSpeedRightWheel(self.speed * ratio)

	def step(self):
		#Récupère l'angle dont ont tourné les roues du robot depuis le début de la stratégie
		self.angle_rotated_left_wheel = self.proxy.getAngleRotatedLeft()
		self.angle_rotated_right_wheel = self.proxy.getAngleRotatedRight()
		self.distance_covered = self.covered_distance()
		if self.stop():
			print("FIN STRATEGIE STEP")
			self.proxy.setSpeed(0)
			return

	def covered_distance(self):
		"""
		calcule la distance parcourue par le robot selon l'angle dont les roues ont tourné
		"""
		distance = (2 * pi * self.proxy.getRadius() ) * (self.angle_rotated_left_wheel / 360) #distance parcourue à partir de l'angle effectué par la roue gauche
		return distance

	def stop(self):
		pas = config.Latest_Dist
		if pas <= SAFE_DISTANCE :
			self.proxy.setSpeed(0)
			print("SAFE DISTANCE STOP !")
			return True
		if self.distance_to_cover >= 0 :
			if self.distance_covered >= self.distance_to_cover:
				self.proxy.setSpeed(0)
				return True
			return False
		else :
			if self.distance_covered <= self.distance_to_cover:
				self.proxy.setSpeed(0)
				return True
			return False

class moveToWallStrategy:
	"""
	Le robot doit atteindre le mur à une vitesse la plus raisonnable sans le toucher.
	"""
	def __init__(self,proxy,speed,wall,to_left_or_right):
		self.proxy = proxy
		self.speed = speed 
		self.wall = wall 
		self.to_left_or_right=to_left_or_right


class Motif1Strategy(StrategySeq) :

	def __init__(self, proxy, speed):
		super().__init__()
		move1 = moveForwardStrategy(proxy, 50, speed )
		move2 = moveForwardStrategy(proxy, 100, speed )
		turnRight = TurnStrategy(proxy, -45, -speed)
		turnLeft = TurnStrategy(proxy, 90, speed)
		self.sequence = [move1, turnRight, move2, turnLeft, move2, turnRight, move1]
			

class Motif2Strategy(StrategySeq) :

	def __init__(self, proxy, speed):
		super().__init__()
		move1 = moveForwardStrategy(proxy, 50, speed )
		move2 = moveForwardStrategy(proxy, 75, speed )
		move3 = moveForwardStrategy(proxy, 100, speed )
		turnRight = TurnStrategy(proxy, -90, -speed)
		turnLeft = TurnStrategy(proxy, 90, speed)
		self.sequence = [move1, turnRight, move2, turnLeft, move3, turnLeft, move2, turnRight, move1]


class RepeatMotif1Strategy() :
	"""
	Effectue le motif1 de manière répétée jusqu'à rencontrer un obstacle, puis fait demi-tour
	et repart en exécutant le même motif, et ainsi de suite
	"""

	def __init__(self, proxy, speed):
		self.move1 = moveForwardStrategy(proxy, 50, speed )
		self.move2 = moveForwardStrategy(proxy, 100, speed )
		self.turnRight = TurnStrategy(proxy, -45, -speed)
		self.turnLeft = TurnStrategy(proxy, 90, speed)
		self.sequence = [self.move1, self.turnRight, self.move2, self.turnLeft, self.move2, self.turnRight, self.move1]
		self.demi_tour = TurnStrategy(proxy, 180, speed)
		self.current_strat = -1
		self.proxy = proxy

	def step(self):
		self.stop() #check si toutes les strat de la seq ont été executées, si c'est le cas, relance la séquence

		if self.current_strat < 0 or self.sequence[self.current_strat].stop(): #démarrage de la prochaine strat
			if (config.obstacle_ahead == True):
				self.sequence = []
				self.sequence = [self.demi_tour, self.move1, self.turnRight, self.move2, self.turnLeft, self.move2, self.turnRight, self.move1] #redémarre la séquence après un demi-tour
				config.obstacle_ahead = False

			self.current_strat += 1
			self.sequence[self.current_strat].start()

		self.sequence[self.current_strat].step()

	def stop(self):
		if self.current_strat == len(self.sequence)-1 and self.sequence[self.current_strat].stop(): #on a atteint la dernière strat et elle est terminée
			#On redémarre la séquence, mais on ne stoppe jamais la stratégie
			self.sequence = [self.move1, self.turnRight, self.move2, self.turnLeft, self.move2, self.turnRight, self.move1]
			self.current_strat = -1

	
