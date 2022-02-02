# -*- coding: UTF-8 -*-
from environment import Environment
from robot import Robot
from obstacle import Obstacle, Wall
from viewer import show2D

#Creation de l'environnement
env = Environment(800,300)

#Tests robot
rob = Robot(300,240)
env.addObject(rob)
print(env.objects)
rob.changeDir(315)

#Tests obstacle
obs = Obstacle(10,50,100,30)
env.addObject(obs)
print(env.objects)
obs2 = Obstacle(250,180,30,100)
env.addObject(obs2)
print(env.objects)

# Ajout d'un mur
mur=Wall(0,0,env.height,90)
mur2=Wall(env.width-5,0,env.height,90)
mur3=Wall(0,0,env.width,0)
mur4=Wall(0,env.height-5,env.width,0)
env.addObject(mur)
env.addObject(mur2)
env.addObject(mur3)
env.addObject(mur4)

#Lance un thread secondaire qui execute updateSimulation() et démarre l'affichage graphique
show2D(env, rob)

