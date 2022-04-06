from .environment import Environment
from .robot import Robot
from .obstacle import Obstacle,Wall

class FoV:
    #FOV pour Field of View : le but est de permettre au robot de pouvoir detecter
    #des obstacles pour éviter la collision
    def __init__(self,degree,length):
        """
            :length:int
            :degree:int
            :safespace:int
        """
        self.degree=degree #degree du champs de vision
        self.length=length #longueur jusqu'à laquelle le robot peut percevoir
        self.collision=False
        self.safespace=0.1
        #self.safespace

    def setSafespace(self,newss): #newss: new safe space
        """
            :newss:int
            Set le safe space de none a newss
        """
        self.safespace=newss
