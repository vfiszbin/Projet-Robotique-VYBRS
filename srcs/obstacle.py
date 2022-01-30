# -*- coding: UTF-8 -*-
class Obstacle:
     def __init__(self,positionX,positionY,width,height):
         """  (positionX,positionY) : les coordonnes du point d'extremites en haut a gauche (pour reperer les obstacles)
         """
         self.positionX=positionX
         self.positionY=positionY
         self.width=width
         self.height=height

#pour l'instant la classe fait des mur 90 et 0 deg uniquement
class wall(Obstacle):
     def __init__(self,positionX,positionY,length,dire):
          if (dire == 90) or (dire==270):
               super().__init__(positionX,positionY,5,length)
          else :
               super().__init__(positionX,positionY,length,5)
