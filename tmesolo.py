# Majdoub Bilel 
# NE : 3800088
# email : bilel.mjdb@gmail.com (mail etudiant)


# exercice 1 : modifications graphiques

#q1.1()
from math import * # bibliotheques mathematiques cos,sin...
from time import time # import pour simuler les threads
TIME = 100 # voir question 1.2.2
class Robot:
    def __init__(self,positionX,positionY,couleur,ID_LED,statut):
        """
        :positionX: int
        :positionY: int
        Représente un robot avec une position initiale (positionX, positionY)
        la couleur represente la couleur initiale du robot
        """
        super().__init__() # appel du constructeur par heritahe
        self.positionX = positionX
        self.positionY = positionY
        self.couleur=couleur
        self.ID_LED=ID_LED
        self.statut=statut 
        self.wheelMode=1 #le robot avance

        # q2.1()
        self.dir=dir
        self.speedLeftWheel = 0 
        self.speedRightWheel = 0
        self.angle_rotated_left_wheel = 0  #angle de rotation de la roue gauche
        self.angle_rotated_right_wheel = 0 # angle de rotation d ela roue droite




def changeCouleurRob(self,couleur):
    """Change la couleur initiale de notre Robot"""

    self.couleur="rose"



#Q1.2()

    #q1.2.1()

    def simumaleurLed(self,ID_LED,statut):
        """ajoute uner led rouge a gauche du robot et une led bleue a droite du robot"""

        if statut==True:
            ID_LED=1
            set_led(ID_LED,statut)
        else:
            ID_LED=0
            set_led(ID_LED,statut)
    
    #q1.2.2()
    class moveForwardStrategy:
        """Strategie qui fait avancer le robot en ligne droite"""

        def __init__(self,proxy,distance,speed):
            self.proxy=proxy
            self.distance=distance
            self.speed=speed
            self.distance_covered=0
            #les angles de rotationd des roues gauches et droites sont mises à 0 ; du fait que le robot n'executera aucun virage à gauche,
            # ni a droite.
            self.angle_rotated_left_wheel = 0
		    self.angle_rotated_right_wheel = 0
            # ces parametres ne seront pas utilises dans cette question.


        def start(self,ID_LED,statut):
            """Parcourt une ligne droite en alternant led ouverte puis led fermee
            """

            self.proxy.setWheelMode(1) # les roues sont mises en mode avancer.
            self.proxy.setSpeed(self.speed) # on donne une vitesse au robot
            # on alterne les alumé puis led eteinte
            if self.stop():
                
                for i in range(0,TIME):
                    self.simulateurLed(1,1)
                    self.simulateurLed(2,1)
                    self.simulateurLed(2,0)
                    self.simulateurLed(1,0)
        def stop(self):
            """ Arreter le parcour du robot"""

            if self.distance >= 0:
			    return self.distance_covered >= self.distance
		    else:
			    return self.distance_covered <= self.distance

# exercice 2 strategies simples

# q2.1()

# on supposera la classe robot reutilisable dans question 1

class movePolygone(moveForwardStrategy):
    """ Realise le motif 1 du sujet """

    def __init__(self,proxy,speed,distance):
        super.__init__(proxy,speed,distance)
        self.proxy=proxy
        self.speed=speed
        self.distance=distance

    def start(self):
        """instancie notre robot simule avant le demarage """

        self.proxy.resetAngleRotated()
		self.proxy.setWheelMode(1) 
		self.proxy.setSpeed(self.speed) # on passe une vitesse au robot au demarage
        
             











