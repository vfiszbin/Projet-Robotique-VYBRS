from math import *
from .obstacle import Obstacle
from time import time



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
        self.dir = 90 #direction par défaut en degrés
        self.speed = 0 #vitesse du robot en Degrés Par Secondes (DPS)
        self.wheelMode = 1
        self.width= 2
        self.height = 2
        self.last_time = time() #pour savoir combien de temps s'est écoulé depuis le dernier update()

        self.radius_of_wheels = 5 #le rayon des roues
        #L'angle dont les deux roues ont tourné depuis le dernier reset. C'est le controleur qui interroge et reset ces deux variables :
        self.angle_rotated_left_wheel = 0
        self.angle_rotated_right_wheel = 0


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


    def updateDir(self, angle_rotated):
        # r = 5 #rayon / DOIT REFLETER LA DISTANCE ENTRE LE CENTRE DU ROBOT ET L'UNE DE SES ROUES !!!
        # alpha = (360 * distance) / (2 * pi * r)
        self.dir += angle_rotated

    def changeSpeed(self, speed):
        self.speed = speed

    #merge les deux fonctions suivantes
    def deplacerRobot(self, angle_rotated):
        """
        :distance: int
        fonction qui deplace  le robot depuis les coordonnées(positionX,positionY) vers l'avant selon l'angle 'dir' et une distance
        """
        dir = self.dir * pi / 180 #conversion des degrés en radians
        distance = (2 * pi * self.radius_of_wheels) * (angle_rotated / 360) #distance parcourue à partir de l'angle effectué par les roues
        dx = distance * cos(dir)
        dy = distance * sin(dir)
        self.positionX = self.positionX + dx
        self.positionY = self.positionY - dy

    def update(self):
        """
        Maj la position ou la direction du robot selon la distance parcourue et le wheelMode du robot
        """
        current_time = time()
        elapsed_time = current_time - self.last_time
        angle_rotated = self.speed * elapsed_time # Angle effectué par les roues = Vitesse (Degrés Par Seconde) * Temps (Secondes)

        if self.wheelMode == 1: #roues en mode 1 pour avancer/reculer
            self.deplacerRobot(angle_rotated)
            self.angle_rotated_left_wheel += angle_rotated
            self.angle_rotated_right_wheel += angle_rotated

        elif self.wheelMode == 2: #roues en mode 2 pour tourner
            self.updateDir(angle_rotated)
            self.angle_rotated_left_wheel -= angle_rotated
            self.angle_rotated_right_wheel += angle_rotated

        self.last_time = time()

    def move(self,positionX,positionY):
        """ int * int -> None
        Deplace le robot de positionX en abscisse et positionY en ordonnee
        """
        self.positionX=positionX
        self.positionY=positionY
        print("Le robot s'est deplace en [", self.positionX, ",", self.positionY, "]")


    def scalairevectoriel(self,xa,ya,xb,yb,xc,yc,xd,yd):
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
            upr = (obj.positionX+obj.height,obj.positionY)
            lowl = (obj.positionX,obj.positionY+obj.width)
            lowr = (obj.positionX+obj.height,obj.positionY+obj.width)

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

            prodvsright=self.scalairevectoriel(robx,roby,dx,dy,xB,yB,xC,yC)
            prodsvright=self.scalairevectoriel(xB,yB,xC,yC,robx,roby,dx,dy)
            prodvsleft=self.scalairevectoriel(robx,roby,dx,dy,xA,yA,xD,yD)
            prodsvleft=self.scalairevectoriel(xA,yA,xD,yD,robx,roby,dx,dy)
            prodvsup=self.scalairevectoriel(robx,roby,dx,dy,xA,yA,xB,yB)
            prodsvup=self.scalairevectoriel(xA,yA,xB,yB,robx,roby,dx,dy)
            prodsvslow=self.scalairevectoriel(robx,roby,dx,dy,xD,yD,xC,yC)
            prodsvlow=self.scalairevectoriel(xD,yD,xC,yC,robx,roby,dx,dy)
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

    def is_outside_of_the_environment(self,positionX, positionY, env):
        """
        :width: float
        :height: float
        Renvoie True si le robot se trouve à l'extérieur des bords de l'environnement et False sinon.
        """
        width = env.width
        height = env.height

        if (positionX < 0) or (positionY > width) or (positionY < 0) or (positionY > height):
            return True
        else:
            return False


    def is_inside_an_obstacle_in_the_environment(self, posX, posY, env):
        """
        :objects: [Obstacles]
        Renvoie True si le robot se trouve à l'intérieur d'un obstacle de l'environnement et False sinon.
        """
        for x in env.objects:
            if isinstance(x, Obstacle):
                if posX >= x.positionX and posX <= (x.positionX + x.width) and posY >= x.positionY and posY <= (x.positionY + x.height):
                    return True
        return False

    def getDistance(self, env):
        """
        :objects: [Obstacles]
        """
        pas=0
        taille_pas = 1
        posX = self.positionX
        posY = self.positionY
        dir = self.dir * pi / 180
        dx = taille_pas * cos(dir)
        dy = taille_pas * sin(dir)

        while(not(self.is_inside_an_obstacle_in_the_environment(posX, posY, env) or self.is_outside_of_the_environment(posX, posY, env))):
            posX+=dx
            posY-=dy
            pas+=1

        return pas
