from simulation.controller.controller import *
from simulation.controller.proxy import ProxySimu, ProxyReal

def initializeProxy(rob, env):

	if config.simu_or_real == 1: #importe proxy simulation
		proxy = ProxySimu(rob, env)
		
	elif config.simu_or_real == 2: #importe proxy réel
		proxy = ProxyReal(rob)

	return proxy

class SetStrategies :

	def __init__(self,rob, env) :
		proxy = initializeProxy(rob,env)

		#Prépare des séquences de stratégies que le controleur va executer
		self.sequences = [] #la liste contenant les séquences de stratégies 
		seq2=StrategySeq(proxy)
		
		#seq=RepeatMotif1Strategy(proxy, 100)
		# s2=moveForwardStrategy(proxy, 500, 30) 
		# s2=TurnStrategy(proxy, 90, 30)
		# s2 = ArcStrategy(proxy, 180, 50, 20, 0)
		# seq2.addStrategy(s2)
		# self.sequences.append(seq2)

		seq = detect_balise(proxy, "B", 50)
		self.sequences.append(seq)

		# seq1 = SquareStrategy(proxy,300,50)
		# self.sequences.append(seq1)
		# seq2=StrategySeq()
		# s1=moveForwardStrategy(proxy,200,50)
		# s2=TurnStrategy(proxy,-70,-80)
		# s3=moveBackwardStrategy(proxy, 250, 30)
		# s4=Navigate(proxy,250,48) # tester avec une plus grande distance pour voir comment se comporte le robot. 
		# seq2.addStrategy(s1)
		# seq2.addStrategy(s2)
		# seq2.addStrategy(s3)
		# seq2.addStrategy(s4)
		# self.sequences.append(seq2)
		
		# m type class MovetoWallSpeedStrategy
		# m = MovetoWallSpeedStrategy(proxy,50)
		# seq3.addStrategy(m)
		# self.sequences.append(seq3)
