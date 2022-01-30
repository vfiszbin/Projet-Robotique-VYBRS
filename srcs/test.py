# -*- coding: UTF-8 -*-
from environment import environment
from robot import robot
from obstacle import Obstacle,wall
from viewer import show2D

<<<<<<< HEAD
#Creation de l'environnement
env = environment(800,300)
=======

#Création de l'environnement
env = environment(400,300)
>>>>>>> 15cfe86be5972c1b53a1358c83fdfa19501d6218

#Tests robot
rob = robot(300,240)
env.addObject(rob)
<<<<<<< HEAD
print(env.objects)
rob.changeDir(90)
=======
#print(env.objects)
rob.changeDir(45)
>>>>>>> 15cfe86be5972c1b53a1358c83fdfa19501d6218

#Tests obstacle
obs = Obstacle(10,50,100,30)
env.addObject(obs)
#print(env.objects)
obs2 = Obstacle(250,180,30,100)
env.addObject(obs2)
<<<<<<< HEAD
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
=======
#print(env.objects)
>>>>>>> 15cfe86be5972c1b53a1358c83fdfa19501d6218

#Lance un thread secondaire qui execute updateSimulation() et démarre l'affichage graphique
show2D(env, rob)


