# -*- coding: UTF-8 -*-
from math import *
from .robot import *

class Obstacle:
    def __init__(self,positionX,positionY,width,height):
        """
        :positionX: int
        :positionX: int
	    :width: int
        :height: int
        Cree un obstacle avec (positionX,positionY) : les coordonnes  int du point d'extremites en haut a gauche.
        """
        self.positionX=positionX
        self.positionY=positionY
        self.width=width
        self.height=height
	
    def getDistance(self):
        """
        Retourne la distance du premier obstacle dans la direction du robot en nombre de pas
        """
        #dx : float
        dx = self.getPositionXRobot()/math.cos(self.getDir())
        #dy : float
        dy = self.getPositionYRobot()/math.sin(self.getDir())
        #d: float
        d = dx+dy
        # Direction
        dir = math.radians(self.getDir)
        #Calcul du point se trouvant à une distance d de la position du robot dans sa direction
        x0 = self.getPositionXRobot()
        y0 = self.getPositionYRobot()
        x1 = x0
        y1 = y0
        # pas : float
        pas = 0

        while not (self.is_outside_of_the_environment(x1,y1) or self.is_inside_an_obstacle_in_the_environment(self.positionX,self.positionY,x1,y1)):
            self.deplacerRobot(d)
            x0 = x1
            y0 = y1
            pas += 1
        return pas
        

#pour l'instant la classe fait des mur 90 et 0 deg uniquement
class Wall(Obstacle):
    """
    classe fille de l'objet obstacle qui cree des obstacle en forme de mur
    """
    def __init__(self,positionX,positionY,length,dire):
        """
        :positionX: int
        :positionX: int
        :length: int
        :dire: int
        Cree un mur depuis (positionX,positionY) de longeur length avec une direction dire
        """
        if (dire == 90) or (dire==270):
            super().__init__(positionX,positionY,5,length)
        else :
            super().__init__(positionX,positionY,length,5)
