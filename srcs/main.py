# -*- coding: UTF-8 -*-
from simulation.modele.environment import Environment
from simulation.modele.obstacle import Obstacle, Wall
from simulation.modele.robot import Robot
from simulation.viewer.view2D import View2D
from simulation.modele.updateModele import UpdateModele
from threading import Thread
from simulation.controller.controller import TestStrategy,Strategy,move,turn


#Creation de l'environnement
env = Environment(800,300)


#Tests robot
rob = Robot(300,240)
env.addObject(rob)
print(env.objects)
rob.changeDir(115)
print(rob.getDir())
print(rob.getPositionXRobot())
print(rob.getPositionYRobot())

#Tests obstacle
obs = Obstacle(10,50,100,30)
env.addObject(obs)
print(env.objects)
obs2 = Obstacle(150,180,30,100)
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

#Lance updateModele qui s'execute dans un thread secondaire
update_modele = UpdateModele(env,rob)
update_modele.start()

#test des  strategie :
s1=move(rob,5,-30)
#Lance le controleur test
controller_thread = Thread(target=TestStrategy, args=(rob,))
controller_thread.start()


#Lance l'affichage graphique 2D de la simulation qui s'execute sur le thread principal
View2D(env)
