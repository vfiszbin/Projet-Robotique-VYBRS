from environment import environment
from robot import robot
from obstacle import Obstacle
from viewer import show2D

#Création de l'environnement
env = environment(400,300)

#Tests robot
rob = robot(300,100)
env.addObject(rob)
print(env.objects)
rob.changeDir(45)

#Tests obstacle
obs = Obstacle(10,50,100,30)
env.addObject(obs)
print(env.objects)
obs2 = Obstacle(250,180,30,100)
env.addObject(obs2)
print(env.objects)

#Affiche la représentation 2D de l'environnement
show2D(env)

# changer la direction du robot 
rob.deplacerPositionRobotAvant(15,-7,45,20)
rob.deplacerPositionRobotDerriere(-30,20,-160,-30)

