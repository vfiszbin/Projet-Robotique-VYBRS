from tkinter import Tk, Canvas
from math import cos, sin, pi
from robot import robot
from obstacle import Obstacle

def show2D(environment):
	window = Tk()
	window.title("Environnement")

	canvas = Canvas(window, height=environment.height, width=environment.width)
	canvas.pack()

	for obj in environment.objects: #représentation visuelle de chaque objet ajouté à l'environnement
		if isinstance(obj, robot):
			#Création d'un cerle pour représenter la position du robot
			r = 3 #rayon
			x = obj.positionX
			y = obj.positionY
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
			canvas.create_line(x0, y0, x1, y1, arrow='last')

		elif isinstance(obj, Obstacle):
			# (x0,y0) = sommet en haut à gauche du rectangle
        	# (x1,y1) = sommet en bas à droite du rectangle 
			x0 = obj.positionX
			y0 = obj.positionY
			x1 = x0 + obj.width
			y1 = y0 + obj.height
			canvas.create_rectangle(x0, y0, x1, y1, fill="grey")

	window.mainloop()