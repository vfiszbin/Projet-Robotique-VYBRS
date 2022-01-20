from tkinter import Tk, Canvas
from robot import robot
from math import cos, sin, pi

class environment:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.objects = [] #liste des objets présents dans l'environnement

    def addObject(self, obj):
        self.objects.append(obj)

    def removeObject(self, obj):
        self.objects.remove(obj)

    def show2D(self):
        window = Tk()
        window.title("Environnement")

        canvas = Canvas(window, height=self.height, width=self.width)
        canvas.pack()

        for obj in self.objects: #représentation visuelle de chaque objet ajouté à l'environnement
            if isinstance(obj, robot):
                #Création d'un cerle pour représenter la position du robot
                r = 3 #rayon
                x = obj.xpos
                y = obj.ypos
                x0 = x - r
                y0 = y - r
                x1 = x + r
                y1 = y + r
                canvas.create_oval(x0, y0, x1, y1, fill="red") 

                #Création d'une flèche représentant la direction du robot
                #Voir Schéma explicatif des calculs de direction
                x0 = x
                y0 = y
                len_arrow = 20
                dir = obj.dir * pi / 180 #conversion des degrés en radians
                dx = len_arrow * cos(dir)
                dy = len_arrow * sin(dir)
                x1 = x0 + dx
                y1 = y0 - dy
                canvas.create_line(x0,y0, x1, y1, arrow='last')

        window.mainloop()