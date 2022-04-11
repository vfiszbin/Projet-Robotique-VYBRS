from simulation.modele.environment import Environment
from simulation.modele.obstacle import Obstacle, Wall
from simulation.modele.robot import Robot


class SetEnvironment : 
	def __init__(self,env,rob) :
		env.addRob(rob)


		# #Ajout des obstacle
		# obs = Obstacle(10,50,100,30)
		# env.addObs(obs)
		# obs2 = Obstacle(600,160,30,100)
		# env.addObs(obs2)

		# obs3 = Obstacle(280,150,40,10)
		# env.addObs(obs3)



		# Ajout des murs
		mur=Wall(0,0,env.height,90)
		mur2=Wall(env.width-5,0,env.height,90)
		mur3=Wall(6,0,env.width-12,0)
		mur4=Wall(6,env.height-5,env.width-12,0)
		env.addObs(mur)
		env.addObs(mur2)
		env.addObs(mur3)
		env.addObs(mur4)
