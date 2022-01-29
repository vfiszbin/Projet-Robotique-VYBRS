from environment import environment
from robot import robot
from viewer import show2D

env = environment(400,300)
rob = robot(200,140, 0)
env.addObject(rob)
print(env.objects)
rob.changeDir(45)
show2D(env)

# # creation de l'objet robot
# R = Robot(0.0,0.0,180)
# # appel de la methode deplacerPositionRobotAvant(self):
# R.deplacerPositionRobotAvant()
# ## appel de la methode deplacerPositionRobotDerriere(self):
# R.deplacerPositionRobotDerriere()
#
# R.changeDirectionRobot()
#
# R.deplaceRobotArgument()
# ###### changer la direction du robot
# R.changeDir(100)
