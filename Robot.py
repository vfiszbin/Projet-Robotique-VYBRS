from math import *
import random
class Robot:
    # creation de mes attributs modifiable si necessaire
    coordX = 0.0 # le robot est au centre du rectangle
    coordY = 0.0 # aux positions nulles.
    #coordZ = 0.0 #### representation en 3d
    direction = pi/180 # direction en degres

    ########## appel a un autre constructeur : notion d'heritage simple
    # instanciation des attributs

    def __init__(self,positionX,positionY,dir):
        super().__init__()
        self.positionX=positionX
        self.positionY=positionY
        self.dir=dir

    def deplacerPositionRobotAvant(self):
        if (self.positionX >= 0. and self.positionY>=0.):
            self.positionX = self.positionX + random.uniform(0.0,20.0)
            self.positionY = self.positionY + random.uniform(0.0,15.0)#### facultatif, peut etre modifie avec la direction du robot
        # dans les autre cas ne rien faire
    def deplacerPositionRobotDerriere(self):
        if (self.positionX < 0. and self.positionY < 0.):
            self.positionX = self.positionX - random.uniform(0.0,20.0)
            self.positionY = self.positionY - random.uniform(0.0,15.0) #### la methode random uniform renvoie un reel compris entre a et b exclus
    def changeDirectionRobot(self):
        if self.deplacerPositionRobotAvant():
            dx = (dx + x)*cos(dir)
        elif self.deplacerPositionRobotAvant():
            dx = (dx - x)*cos(dir)
        elif self.deplacerPositionRobotDerriere():
            dy = (dy + y)*sin(dir)
        elif self.deplacerPositionRobotDerriere():
            dy = (dy - y)*sin(dir)


# creation de l'objet robot
R = Robot(0.0,0.0,180)
# appel de la methode deplacerPositionRobotAvant(self):
R.deplacerPositionRobotAvant()
## appel de la methode deplacerPositionRobotDerriere(self):
R.deplacerPositionRobotDerriere()

R.changeDirectionRobot()
