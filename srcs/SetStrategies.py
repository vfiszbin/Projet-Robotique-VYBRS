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
		seq1 = SquareStrategy(proxy,300,50)
		self.sequences.append(seq1)
		seq2=StrategySeq()
		s1=moveForwardStrategy(proxy,200,50)
		s2=TurnStrategy(proxy,-70,-80)
		s3=moveBackwardStrategy(proxy, 250, 30)
		seq2.addStrategy(s1)
		seq2.addStrategy(s2)
		seq2.addStrategy(s3)
		self.sequences.append(seq2)
