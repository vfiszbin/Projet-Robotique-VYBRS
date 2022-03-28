from simulation.controller.controller import *
from simulation.modele.robot import Robot
from simulation.modele.robot import Robot


class SetStrategies :

	def __init__(self,rob) :
		#Prépare des séquences de stratégies que le controleur va executer
		self.sequences = [] #la liste contenant les séquences de stratégies
		seq1 = SquareStrategy(rob,300,50)
		self.sequences.append(seq1)
		seq2=StrategySeq(rob)
		s1=moveForwardStrategy(rob,200,50)
		s2=TurnStrategy(rob,-70,-80)
		s3=moveBackwardStrategy(rob, 250, 30)
		s4=Navigate(rob,250,200) # tester avec une plus grande distance pour voir comment se comporte le robot. 
		seq2.addStrategy(s1)
		seq2.addStrategy(s2)
		seq2.addStrategy(s3)
		seq2.addStrategy(s4)
		self.sequences.append(seq2)
