class FoV:
    #FOV pour Field of View : le but est de permettre au robot de pouvoir detecter
    #des obstacles pour éviter la collision
    def __init__(self,degree,length):
        """
        """
        self.degree=degree #degree du champs de vision
        self.length=length #longueur jusqu'à laquelle le robot peut percevoir
        self.collision=false
        self.safespace=None
        #self.safespace

    def addObstacle(object,collision):
        """
        """
        #est ce qu'on peut rendre la methode pour ajouter des objets dans l'environnement statique ?
        if(collision):
            Environnement.objects.append(object)

    def calculCollision(self):
        """
        """
        

    def defCollision():
        """
        """
        if(length<safespace):#utiliser le safespace ?
            collision=true
        if(length>=safespace):
            collision=false
