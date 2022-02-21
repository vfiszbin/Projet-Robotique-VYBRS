from math import *
from .obstacle import Obstacle

class Robot:

    ########## appel a un autre constructeur : notion d'heritage simple
    # instanciation des attributs

    def __init__(self,positionX,positionY):
        """
        :positionX: int
        :positionY: int
        Représente un robot avec une position initiale (positionX, positionY)
        """
        super().__init__()
        self.positionX = positionX
        self.positionY = positionY
        self.dir = 90 #direction par défaut
        self.speed = 0

    def changeDir(self, dir):
        """
        :dir: int
        fonction qui change la direction du robot selon l'angle 'dir'
        """
        if dir >= 0 and dir <= 360:
            self.dir = dir
        else:
            print(f"La direction doit être comprise entre 0 et 360 degrés. Retour à la direction par défaut : {self.dir}°")

    def changeSpeed(self, speed):
        self.speed = speed

    #merge les deux fonctions suivantes
    def deplacerPositionRobotAvant(self,distance):
        """
        :positionX: int
        :positionX: int
	    :dir: int
        :distance: int
        fonction qui deplace  le robot depuis les coordonnées(positionX,positionY) vers l'avant selon l'angle 'dir' et une distance
        """
        dir = self.dir * pi / 180 #conversion des degrés en radians
        dx = distance * cos(dir)
        dy = distance * sin(dir)
        self.positionX = self.positionX + dx
        self.positionY = self.positionY - dy


    def deplacerPositionRobotArriere(self,distance):
        """
        :positionX: int
        :positionX: int
	    :dir: int
        :distance: int
        fonction qui déplace  le robot depuis les coordonnées(positionX,positionY) vers l'arriere selon l'angle 'dir' et une distance
	    """
        opposite_dir = (self.dir * pi / 180) + pi #conversion des degrés en radians + on ajoute pi pour obtenir la direction inverse
        dx = distance * cos(opposite_dir)
        dy = distance * sin(opposite_dir)

        self.positionX = self.positionX + dx
        self.positionY = self.positionY - dy

   
    def move(self,positionX,positionY):
        """ int * int -> None
        Deplace le robot de positionX en abscisse et positionY en ordonnee
        """
        self.positionX=positionX
        self.positionY=positionY
        print("Le robot s'est deplace en [", self.positionX, ",", self.positionY, "]")


    def getPositionXRobot(self):
        """
        Retourne la coordonnee x actuelle du robot
        """
        return self.positionX

    def getPositionYRobot(self):
        """
        Retourne la coordonnee y actuelle du robot
        """
        return self.positionY

    def getDir(self):
        """
        Retourne la direction actuelle du robot
        """
        return self.dir

    def detecteObstacle(self,obj):
        """
        :obj:obstacle
        Retourne un booleen, True si le robot se trouve devant un obstacle, False sinon
        """
        if isinstance(obj,Obstacle):
            upl = (obj.positionX,obj.positionY)
            upr = (obj.positionX+obj.length,obj.positionY)
            lowl = (obj.positionX,obj.positionY+obj.width)
            lowr = (obj.positionX+obj.length,obj.positionY+obj.width)

            roba = self.positionX
            robb = self.positionY

            dir = self.dir * pi / 180
            dx =  roba * cos(dir) + robb * sin(dir)
            dy = roba * sin(dir) + robb * cos(dir)

            xA,yA=upl
            xB,yB=upr
            xC,yC=lowr
            xD,yD=lowl

            k = 1

            normeAB=maths.sqrt((xB-xA)*(xB-xA)+(yB-yA)*(yB-yA))
            normeAD=math.sqrt((xD-xA)*(xD-xA)+(yD-yA)*(yD-yA))
            normeBC=math.sqrt((xB-xC)*(xB-xC)+(yB-yC)*(yB-yC))

            normeCD=mqth.sqrt((xD-xC)*(xD-xC)+(yD-yC)*(yD-yC))
            prodvsright=0
            prodsvright=0
            prodvsleft=0
            prodsvleft=0
            prodvsup=0
            prodsvup=0
            prodsvslow=0
            prodsvlow=0
            #<============================================================
            if(prodvsleft<0 and prodsvleft<0):
                return True
            #>============================================================
            if(prodvsright<0 and prodsvright<0):
                return True
            #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            if(prodvsup<0 and prodsvup<0):
                return True
            #-------------------------------------------------------------
            if(prodvslow<0 and prodsvlow<0):
                return True
            else:
                return False
            ####
