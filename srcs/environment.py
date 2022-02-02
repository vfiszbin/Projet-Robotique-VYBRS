from robot import Robot
from obstacle import Obstacle

class Environment:
    def __init__(self, width, height):
        """
        :width: int
        :length: int
        Cree l'enveronemment de dimensions width x height
        """
        if (width <= 0 or height <= 0):
            self.height = 300
            self.width = 400
            print(f"Dimensions invalides, retour aux dimensions par défaut (largeur={self.width},hauteur={self.height})")
        else:
            self.height = height
            self.width = width
        self.objects = [] #liste des objets présents dans l'environnement

    def addObject(self, obj):
        """
        :obj:object
        fonction statique qui prends un objet obj et l'ajoute à l'environnement
        """
        #Vérifie que l'objet robot a des coordonnées compatibles avec cet environnement
        if isinstance(obj, Robot):
            x = obj.positionX
            y = obj.positionY
            if (x < 0 or x > self.width or y < 0 or y > self.height):
                print(f"Coordonnées ({x},{y}) du robot incompatibles avec les dimensions (largeur={self.width},hauteur={self.height}) de l'environnement")
            else:
                self.objects.append(obj)

        #Vérifie que l'objet obstacle a des dimensions compatibles avec cet environnement
        # (x0,y0) = sommet en haut à gauche du rectangle
        # (x1,y1) = sommet en bas à droite du rectangle
        elif isinstance(obj, Obstacle):
            x0 = obj.positionX
            y0 = obj.positionY
            x1 = x0 + obj.width
            y1 = y0 + obj.height
            if (x0 < 0 or x0 > self.width or y0 < 0 or y0 > self.height\
            or x1 < 0 or x1 > self.width or y1 < 0 or y1 > self.height):
                print(f"Dimensions (({x0},{y0}),largeur={obj.width},hauteur={obj.height}) de l'obstacle incompatibles avec celles (largeur={self.width},hauteur={self.height}) de l'environnement")
            else:
                self.objects.append(obj)

    def removeObject(self, obj):
        """
        :obj:object
        fonction statique qui enlève un objet obj de l'environnement
        """
        self.objects.remove(obj)
