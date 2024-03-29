# -*- coding: UTF-8 -*-
from math import *
from .robot import *

class Obstacle:
    def __init__(self,positionX,positionY,width,height):
        """
        :positionX: int
        :positionY: int
	    :width: int
        :height: int
        Cree un obstacle avec (positionX,positionY) : les coordonnes  int du point d'extremites en haut a gauche.
        """
        self.positionX=positionX
        self.positionY=positionY
        self.width=width
        self.height=height


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
