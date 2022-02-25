from time import sleep

UPDATE_TIME = 1 

def TestStrategy(rob):
	sleep(2)
	rob.changeWheelMode(2)
	rob.changeSpeed(100)
	sleep(1)
	rob.changeSpeed(0)
	sleep(1)
	rob.changeSpeed(-120)
	sleep(1)
	rob.changeSpeed(0)
	sleep(1)
	rob.changeSpeed(380)
	sleep(1)
	rob.changeSpeed(0)

	rob.changeWheelMode(1)
	rob.changeSpeed(360)
	sleep(5)
	rob.changeSpeed(0)
	rob.changeWheelMode(2)
	rob.changeSpeed(-260)
	sleep(1)
	rob.changeWheelMode(1)
	rob.changeSpeed(360)
	sleep(3)
	rob.changeSpeed(0)
	rob.changeSpeed(-180)
	sleep(3)
	rob.changeSpeed(0)

def launchStrategySeq(rob):
	strat = StrategySeq()
	while not strat.stop():
		strat.step()
		sleep(1./UPDATE_TIME)

class StrategySeq :
	"""
	classe qui organise des séquences de strategie
	"""
	def __init__(self):
		self.sequence=[]
		self.current_strat = -1

	def addStrategy(self,strat):
		self.sequence.append(strat)

	def removeStrategy(self,strat):
		self.sequence.remove(strat)

	def step(self):
		if self.stop(): #toutes les strat de la seq ont été executés
			return

		if self.current_strat < 0 or self.sequence[self.current_strat].stop(): #démarrage de la prochaine strat
			self.current_strat+=1
			self.sequence[self.current_strat].start()

		self.sequence[self.current_strat].step()

	def stop(self):
		return self.current_strat == len(self.sequence)-1 and self.sequence[self.current_strat].stop() #on a atteint la dernière strat et elle est terminée

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


# class turn(Strategy):
# 	"""
# 	class de strategie: permet de tourner le robot	et l'avancer
# 	"""
# 	def __init__(self,rob,dir):
# 		super().__init__()
# 		self.dir=dir
# 		self.rob=rob
# 	def start(self):
# 		self.begin=True
# 		self.rob.changeDir(self.dir)
# 	def stop(self):
# 		if (rob.getDir()==self.dir) :
# 			self.end = True
# 		else :
# 			print("fail")


# class TurnStrategy:
# 	def __init__(self, distance):
# 		self.dist_to_cover = distance

# 	def start(self):
# 		self.dist_covered = 0

# 	def step(self):
# 		self.dist_covered += 	
# 		if self.stop(): return
# 		self.avancer()

# 	def stop(self):
# 		return self.parcouru>self.distance
