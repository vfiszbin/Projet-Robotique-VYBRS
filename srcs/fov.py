from environment import Environment
from robot import Robot
from obstacle import Obstacle,Wall

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
        self.collision=false
        self.safespace=None
        #self.safespace

    def setSafespace(newss): #newss: new safe space
        """
            :newss:int

        """
        self.safespace=newss

    def addObstacle(object,collision):
        """
            :collision:bool
        """
        #est ce qu'on peut rendre la methode pour ajouter des objets dans l'environnement statique ?
        if(collision):
            robot.listobjects.append(object)


    def calculCollision(self):
        """
        """


    def defCollision():
        """
        """
        if(self.length<self.safespace):#utiliser le safespace ?
            self.collision=true
        if(length>=safespace):
            self.collision=false

    def securiteCollision(robot):
        """:robot:Robot
        """
        if(!self.collision):
