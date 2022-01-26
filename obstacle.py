class Obstacle:
     def __init__(self,positionX,positionY,width,length):
         """  (positionX,positionY) : les coordonnes du point d'extremites en haut a gauche (pour reperer les obstacles)
         """
         self.positionX=positionX
         self.positionY=positionY
         self.width=width
         self.length=length
