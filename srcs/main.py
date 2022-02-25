
from simulation.modele.environment import Environment
from simulation.modele.obstacle import Obstacle, Wall
from simulation.modele.robot import Robot
from simulation.viewer.view2D import View2D
from simulation.modele.updateModele import UpdateModele
from threading import Thread
from simulation.controller.controller import TestStrategy,Strategy,move


#Creation de l'environnement
env = Environment(800,300)

#Tests robot
rob = Robot(300,240)
env.addRob(rob)
print(env.objects)
rob.changeDir(115)
print(rob.getDir())
print(rob.getPositionXRobot())
print(rob.getPositionYRobot())


#Tests obstacle
obs = Obstacle(10,50,100,30)
env.addObs(obs)
print(env.objects)
#obs2 = Obstacle(15,77,30,100)
obs2 = Obstacle(150,180,30,100)
env.addObs(obs2)
print(env.objects)



# Ajout d'un mur
mur=Wall(0,0,env.height,90)
mur2=Wall(env.width-5,0,env.height,90)
mur3=Wall(6,0,env.width-12,0)
mur4=Wall(6,env.height-5,env.width-12,0)
env.addObs(mur)
env.addObs(mur2)
env.addObs(mur3)
env.addObs(mur4)

#Lance updateModele qui s'execute dans un thread secondaire
update_modele = UpdateModele(env,rob)
update_modele.start()

#test des  strategie :
#s1=turn(rob,54)
#Lance le controleur test
controller_thread = Thread(target=TestStrategy, args=(rob,))
#controller_thread = Thread(s1)
controller_thread.start()

#Lance l'affichage graphique 2D de la simulation qui s'execute sur le thread principal
View2D(env)
