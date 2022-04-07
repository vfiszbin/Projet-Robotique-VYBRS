from math import *
from .obstacle import Obstacle
from time import time
from ..lib import getdistancePoints,centreline

WHEEL_DIAMETER = 66.5 #en mm, tiré de l'attribut WHEEL_DIAMETER du vrai robot
WHEEL_BASE_WIDTH = 130 #en mm, distance entre les roues du robot, tiré de l'attribut WHEEL_BASE_WIDTH du vrai robot


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
        self.speedLeftWheel = 0 #vitesse du robot en Degrés Par Secondes (DPS)
        self.speedRightWheel = 0
        self.wheelMode = 1
        self.width= 2
        self.height = 2
        self.last_time = time() #pour savoir combien de temps s'est écoulé depuis le dernier update()

        self.radius_of_wheels = WHEEL_DIAMETER / 2 #le rayon des roues
        self.half_dist_between_wheels = WHEEL_BASE_WIDTH / 2 #distance entre le centre du robot et l'une de ses roues
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
        if wheelMode == 1 or wheelMode == 2 or wheelMode == 3:
            self.wheelMode = wheelMode
        else:
            #print(f"Le mode {wheelMode} est incorrect, il doit être égal à 1 ou 2")
            pass


    def updateDir(self, angle_rotated):
        distance = (2 * pi * self.radius_of_wheels ) * (angle_rotated/ 360) #distance parcourue à partir de l'angle effectué par les roues
        r = self.half_dist_between_wheels #rayon / DOIT REFLETER LA DISTANCE ENTRE LE CENTRE DU ROBOT ET L'UNE DE SES ROUES !!!
        angle_rotated_by_robot = (360 * distance) / (2 * pi * r)
        self.dir += angle_rotated_by_robot

    def changeSpeed(self, speed):
        self.speedLeftWheel = speed
        self.speedRightWheel = speed

    def setSpeedLeftWheel(self, speed):
        self.speedLeftWheel = speed

    def setSpeedRightWheel(self, speed):
        self.speedRightWheel = speed

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

    def deplacerEnArcRobot(self, angle_rotated_left_wheel, angle_rotated_right_wheel):
        """
        fonction qui deplace le robot depuis les coordonnées(positionX,positionY) en arc de cercle
        """
        #calcule la position de départ de la roue gauche (point d)
        dir = (self.dir + 90) * pi / 180 #conversion des degrés en radians. dir est la direction du centre du robot vers la roue gauche
        dist_to_wheelX = self.half_dist_between_wheels * cos(dir)
        dist_to_wheelY = self.half_dist_between_wheels * sin(dir)
        dx = self.positionX + dist_to_wheelX
        dy = self.positionY - dist_to_wheelY

        # print("dir=" + str(dir))
        # print("dist_to_wheelX =" + str(dist_to_wheelX))
        # print("dx =" + str(dx))
        # print("dy =" + str(dy))

        #calcule la position de départ de la roue droite (point b)
        dir = (self.dir - 90) * pi / 180 #conversion des degrés en radians. dir est la direction du centre du robot vers la roue droite
        dist_to_wheelX = self.half_dist_between_wheels * cos(dir)
        dist_to_wheelY = self.half_dist_between_wheels * sin(dir)
        bx = self.positionX + dist_to_wheelX
        by = self.positionY - dist_to_wheelY

        # print("bx =" + str(bx))
        # print("by =" + str(by))

        #calcule la distance parcourue par la roue gauche
        dg = (2 * pi * self.radius_of_wheels) * (angle_rotated_left_wheel / 360) #distance parcourue à partir de l'angle effectué par la roue

        #calcule la distance parcourue par la roue droite
        dd = (2 * pi * self.radius_of_wheels) * (angle_rotated_right_wheel / 360)

        # print("dg =" + str(dg))
        # print("dd =" + str(dd))

        ratio = dg / dd


        db = WHEEL_BASE_WIDTH #distance entre d et b (c'est la dist entre les roues dans les 2 cas)
        ad = - ((db * ratio) / (ratio - 1)) #distance entre a l'origine de l'arc de cercle décrit par le robot et e

        # print("db =" + str(db))
        # print("ad =" + str(ad))
    
        ec = WHEEL_BASE_WIDTH #distance entre e et c est égale à celle entre d et b 
        ae = - ((ec * ratio) / (ratio - 1)) #distance entre a l'origine de l'arc de cercle décrit par le robot et e

        # print("ec =" + str(ec))s
        # print("ae =" + str(ae))

        # print("dg =" + str(dg))
        # print("ae =" + str(ae))
        alpha = (360 * dg)  / (2 * pi * ae) #angle de l'arc de cercle décrit

        # print("alpha=" + str(alpha))
       
        #calcule position de l'origine
        dir = (self.dir + 90) * pi / 180 #conversion des degrés en radians. dir est la direction du centre du robot vers l'origine du cercle
        dist_X = ad * cos(dir)
        dist_Y = ad * sin(dir)
        ax = dx + dist_X
        ay = dy - dist_Y
        
        # print("dir=" + str(dir))
        # print("ad =" + str(ad))
        # print("dist_X =" + str(dist_X))
        # print("ax =" + str(ax))
        # print("ay =" + str(ay))


        #calcule position de fin de la roue gauche (point e)
        alpha = alpha * pi / 180 #conversion des degrés en radians
        dist_X = ae * cos(alpha)
        dist_Y = ae * sin(alpha)
        ex = ax + dist_X
        ey = ay - dist_Y

        # print("ex =" + str(ex))
        # print("ey =" + str(ey))


        #calcule position de fin de la roue droite (point c)
        ac = ae + ec
        dist_X = ac * cos(alpha)
        dist_Y = ac * sin(alpha)
        cx = ax + dist_X
        cy = ay - dist_Y



        pos_robot = centreline(ex, ey, cx, cy) #retourne le couple de la position finale du robot (milieu de la pos finale des roues)
        # print("pos_robot =" + str(pos_robot))

        #Maj la position du robot
        self.positionX = pos_robot[0]
        self.positionY = pos_robot[1]

        # dir = self.dir * (pi / 180)
        # alpha = (dd - dg) / WHEEL_BASE_WIDTH + dir
        self.dir = self. dir - alpha * (180 / pi) #maj la direction du robot

        # print("self.positionX =" + str(self.positionX))
        # print("self.positionY =" + str(self.positionY))

    def deplacerEnArcRobot2(self, angle_rotated_left_wheel, angle_rotated_right_wheel):

        #calcule la distance parcourue par la roue gauche
        dg = (2 * pi * self.radius_of_wheels) * (angle_rotated_left_wheel / 360) #distance parcourue à partir de l'angle effectué par la roue

        #calcule la distance parcourue par la roue droite
        dd = (2 * pi * self.radius_of_wheels) * (angle_rotated_right_wheel / 360)

        dir = self.dir * (pi / 180)
        alpha = (dd - dg) / WHEEL_BASE_WIDTH + dir

        self.positionX = self.positionX + ( (WHEEL_BASE_WIDTH * (dd + dg)) / (2 * (dd - dg)) ) * ( sin(alpha) - sin(dir) )
        self.positionY = self.positionY + ( (WHEEL_BASE_WIDTH * (dd + dg)) / (2 * (dd - dg)) ) * ( cos(alpha) - cos(dir) )

        self.dir = alpha * (180 / pi) #maj la direction du robot


    def deplacerEnArcRobot3(self, angle_rotated_left_wheel, angle_rotated_right_wheel):

        #calcule la distance parcourue par la roue gauche
        dg = (2 * pi * self.radius_of_wheels) * (angle_rotated_left_wheel / 360) #distance parcourue à partir de l'angle effectué par la roue

        #calcule la distance parcourue par la roue droite
        dd = (2 * pi * self.radius_of_wheels) * (angle_rotated_right_wheel / 360)

        s = (dd + dg) / 2
        dir = self.dir * (pi / 180)
        alpha = (dd - dg) / WHEEL_BASE_WIDTH + dir

        self.positionX = s * cos(alpha) + self.positionX
        self.positionY = -(s * sin(alpha)) + self.positionY

        self.dir = alpha * (180 / pi)



    def update(self):
        """
        Maj la position ou la direction du robot selon la distance parcourue et le wheelMode du robot
        """
        current_time = time()
        elapsed_time = current_time - self.last_time
        angle_rotated_left_wheel = self.speedLeftWheel * elapsed_time # Angle effectué par la roue = Vitesse (Degrés Par Seconde) * Temps (Secondes)

        if self.wheelMode == 1: #roues en mode 1 pour avancer/reculer
            self.deplacerRobot(angle_rotated_left_wheel)
            self.angle_rotated_left_wheel += angle_rotated_left_wheel
            self.angle_rotated_right_wheel += angle_rotated_left_wheel

        elif self.wheelMode == 2: #roues en mode 2 pour tourner
            self.updateDir(angle_rotated_left_wheel)
            self.angle_rotated_left_wheel -= angle_rotated_left_wheel
            self.angle_rotated_right_wheel += angle_rotated_left_wheel

        elif self.wheelMode == 3: #roues en mode 3 pour tracer un arc de cercle
            angle_rotated_right_wheel = self.speedRightWheel * elapsed_time
            self.deplacerEnArcRobot(angle_rotated_left_wheel, angle_rotated_right_wheel)
            self.angle_rotated_left_wheel += angle_rotated_left_wheel
            self.angle_rotated_right_wheel += angle_rotated_right_wheel
            # print("angle_rotated_left=" + str(self.angle_rotated_left_wheel))
            # print("angle_rotated_right=" + str(self.angle_rotated_right_wheel))

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
            if(prodsvslow<0 and prodsvlow<0):
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
