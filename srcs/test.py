# -*- coding: UTF-8 -*-
from environment import environment
from robot import robot
from obstacle import Obstacle,wall
from viewer import show2D

#Creation de l'environnement
env = environment(800,300)

#Tests robot
rob = robot(300,240)
env.addObject(rob)
print(env.objects)
rob.changeDir(90)

#Tests obstacle
obs = Obstacle(10,50,100,30)
env.addObject(obs)
print(env.objects)
obs2 = Obstacle(250,180,30,100)
env.addObject(obs2)
print(env.objects)

# Ajout d'un mur 
mur=wall(0,0,300,90)
mur2=wall(795,0,300,90)
mur3=wall(0,0,800,0)
mur4=wall(0,295,800,0)
env.addObject(mur)
env.addObject(mur2)
env.addObject(mur3)
env.addObject(mur4)

#Affiche la representation 2D de l'environnement
show2D(env)

# changer la direction du robot 
rob.deplacerPositionRobotAvant(15,-7,45,20)
rob.deplacerPositionRobotDerriere(-30,20,-160,-30)


