from math import cos,sin

class robot:

    ########## appel a un autre constructeur : notion d'heritage simple
    # instanciation des attributs

    def __init__(self,positionX,positionY):
        """ 
        :positionX: int
        :positionY: int
        Représente un robot avec une position initiale (positionX, positionY) 
        """
        super().__init__()
        self.positionX=positionX
        self.positionY=positionY
        self.dir= 90 #direction par défaut
        
    def changeDir(self, dir):
        """ 
        :dir: int
        fonction qui change la direction du robot selon l'angle 'dir' 
        """
        if dir >= 0 and dir <= 360:
            self.dir = dir
        else:
            print(f"La direction doit être comprise entre 0 et 360 degrés. Retour à la direction par défaut : {self.dir}°")

    def deplacerPositionRobotAvant(self,positionX,positionY,dir,distance):
        dx=distance*cos(dir)
        dy=distance*sin(dir)
        self.positionX = positionX+dx
        self.positionY = positionY-dy
    
    def deplacerPositionRobotDerriere(self,positionX,positionY,dir,distance):
        dx=-distance*cos(dir)
        dy=distance*sin(dir)
        self.positionX = positionX+dx
        self.positionY = positionY-dy   
