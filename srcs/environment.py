from turtle import width
from robot import robot

class environment:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.objects = [] #liste des objets présents dans l'environnement

    def addObject(self, obj):
        #Vérifie que l'objet robot a des coordonnées compatibles avec cet environnement
        if isinstance(obj, robot):
            x = obj.positionX
            y = obj.positionY
            if (x < 0 or x > self.width or y < 0 or y > self.height):
                print(f"Coordonnées ({x},{y}) du robot incompatibles avec les dimensions (largeur={self.width},hauteur={self.height}) de l'environnement")
            else:
                self.objects.append(obj)

    def removeObject(self, obj):
        self.objects.remove(obj)
    
