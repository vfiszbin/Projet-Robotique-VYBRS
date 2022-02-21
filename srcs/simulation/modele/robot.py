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
        self.wheelMode = 1

    def changeDir(self, dir):
        """
        :dir: int
        fonction qui change la direction du robot selon l'angle 'dir'
        """
        self.dir = dir

    # 2 modes pour les roues : mode 1 (avancer/reculer) et 2 (tourner)
    # Mode 1 : les deux roues vont dans le même sens, on donc peut avancer avec une vitesse positive ou reculer avec une vitesse négative
    # Mode 2 : les deux roues tournent en sens opposés, le robot tourne sur lui même
    def changeWheelMode(self, wheelMode):
        if wheelMode == 1 or wheelMode == 2:
            self.wheelMode = wheelMode
        else:
            print(f"Le mode {wheelMode} est incorrect, il doit être égal à 1 ou 2")
    
    def updateDir(self, distance):
        r = 3 #rayon
        alpha = (360 * distance) / (2 * pi * r)
        self.dir += alpha

    def changeSpeed(self, speed):
        self.speed = speed

    #merge les deux fonctions suivantes
    def deplacerRobot(self,distance):
        """
        :distance: int
        fonction qui deplace  le robot depuis les coordonnées(positionX,positionY) vers l'avant selon l'angle 'dir' et une distance
        """
        dir = self.dir * pi / 180 #conversion des degrés en radians
        dx = distance * cos(dir)
        dy = distance * sin(dir)
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

    def scalairevectoriel(xa,ya,xb,yb,xc,yc,xd,yd):
        """
        :xa:int
        :ya:int
        :xb:int
        :yb:int
        :xc:int
        :yc:int
        :xd:int
        :yd:int
        Retourne (AB/\AC)(AB/\AD)
        """
        return (xa*yb-ya*xb)*(xc*yd-xd*yc)

    def detecteCollision(self,obj):
        """
        :obj:obstacle
        Retourne un booleen, True si le robot est en collision avec un obstacle, False sinon
        """
        if isinstance(obj,Obstacle):
            upl = (obj.positionX,obj.positionY)
            upr = (obj.positionX+obj.length,obj.positionY)
            lowl = (obj.positionX,obj.positionY+obj.width)
            lowr = (obj.positionX+obj.length,obj.positionY+obj.width)

            robx = self.positionX
            roby = self.positionY

            dir = self.dir * pi / 180
            dx =  robx * cos(dir) + roby * sin(dir)
            dy = robx * sin(dir) + roby * cos(dir)

            xA,yA=upl
            xB,yB=upr
            xC,yC=lowr
            xD,yD=lowl

#            normeAB=maths.sqrt((xB-xA)*(xB-xA)+(yB-yA)*(yB-yA))
#            normeAD=math.sqrt((xD-xA)*(xD-xA)+(yD-yA)*(yD-yA))
#            normeBC=math.sqrt((xB-xC)*(xB-xC)+(yB-yC)*(yB-yC))
#            normeCD=math.sqrt((xD-xC)*(xD-xC)+(yD-yC)*(yD-yC))

            prodvsright=scalairevectoriel(robx,roby,dx,dy,xB,yB,xC,yC)
            prodsvright=scalairevectoriel(xB,yB,xC,yC,robx,roby,dx,dy)
            prodvsleft=scalairevectoriel(robx,roby,dx,dy,xA,yA,xD,yD)
            prodsvleft=scalairevectoriel(xA,yA,xD,yD,robx,roby,dx,dy)
            prodvsup=scalairevectoriel(robx,roby,dx,dy,xA,yA,xB,yB)
            prodsvup=scalairevectoriel(xA,yA,xB,yB,robx,roby,dx,dy)
            prodsvslow=scalairevectoriel(robx,roby,dx,dy,xD,yD,xC,yC)
            prodsvlow=scalairevectoriel(xD,yD,xC,yC,robx,roby,dx,dy)
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

    def is_outside_of_the_environment(self,width, height):
        """
        :x: float
        :y: float
        Renvoie True si le robot se trouve se trouve à l'extérieur des bords de l'environnement et False sinon.
        """
        if (self.positionX < 0) or (self.positionY > width) or (self.positionY < 0) or (self.positiony > height):
            return True
        else:
            return False


    def is_inside_an_obstacle_in_the_environment(self,objects):
        """
        :x: float
        :y: float
        Renvoie True si le robot se trouve à l'intérieur d'un obstacle de l'environnement et False sinon.
        """

        for obj in objects :

            if isinstance (obj,Obstacle):

                if (obj.positionX<= self.positionX<= obj.positionX + obj.width) and (obj.positionY <= self.positionY <= obj.positionYs + obj.height):
                    return True

            return False
