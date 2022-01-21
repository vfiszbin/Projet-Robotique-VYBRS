import random
class Robot:
    # creation de mes attributs modifiable si necessaire
    coordX = 0.0 # le robot est au centre du rectangle
    coordY = 0.0 # aux positions nulles.
    #coordZ = 0.0

    # instanciation des attributs

    def __init__(self,positionX,positionY):
        self.positionX=positionX
        self.positionY=positionY

    def deplacerPositionRobotAvant(self):
        if (self.positionX >= 0. and self.positionY>=0.):
            self.positionX = self.positionX + random.uniform(0.0,20.0)
            self.positionY = self.positionY + random.uniform(0.0,15.0)
        # dans les autre cas ne rien faire

# creation de l'objet robot
R = Robot(0.0,0.0)
# appel de la methode deplacerPositionRobotAvant(self):
R.deplacerPositionRobotAvant()
