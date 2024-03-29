from tkinter import Tk, Canvas
from math import cos, sin, pi
from ..modele.robot import Robot
from ..modele.obstacle import Obstacle
from .. import config

UPDATE_FREQUENCY = 100 #en millisecondes


# 	L'affichage graphique avec tkinter requiert de lancer une mainloop() qui va bloquer l'execution de toute autre instructions (c'est équivalent à
# 	une boucle while infinie). Pour continuer à executer d'autres instructions que l'affichage graphique on lance updateModele()
# 	dans un thread secondaire qui s'execute en parallèle de l'affichage graphique.	
class View2D:
	def __init__(self, environment):
		self.window = Tk()
		self.window.title("Environnement")
		self.environment = environment
		self.canvas = Canvas(self.window, height=environment.height, width=environment.width)
		self.canvas.pack()

		self.window.after(1000, self.update) #commence à executer update() dans 1000 ms

		self.window.mainloop() # bloque le main thread
		config.run = False #indique aux boucles while du programme de prendre fin à la fermeture de la fenêtre Tkinter

	def update(self):
		'''
		Une fois l'affichage graphique lancé en appelant mainloop(), l'execution de code est bloquée dans le main thread,
		on utilise donc after() qui va appeler cette fonction toutes les x ms pour mettre à jour l'affichage graphique
		'''
		self.canvas.delete("all") # efface tous les objets déjà affichés, cela évite de créer des doubles
		for obj in self.environment.objects: #représentation visuelle de chaque objet ajoutée à l'environnement
			if isinstance(obj, Robot):
				self.displayRobot(obj)

			elif isinstance(obj, Obstacle):
				self.displayObstacle(obj)

		self.window.after(UPDATE_FREQUENCY, self.update) # update() se rappelle elle même toutes les x ms

	def displayRobot(self, rob):
		#Création d'un cerle pour représenter la position du robot
		r = 3 #rayon
		x = rob.positionX
		y = rob.positionY
		x0 = x - r
		y0 = y - r
		x1 = x + r
		y1 = y + r
		self.canvas.create_oval(x0, y0, x1, y1, fill="red")

		#Création d'une flèche représentant la direction du robot
		#Voir Schéma explicatif des calculs de direction
		x0 = x
		y0 = y
		len_arrow = 20
		dir = rob.dir * pi / 180 #conversion des degrés en radians
		dx = len_arrow * cos(dir)
		dy = len_arrow * sin(dir)
		x1 = x0 + dx
		y1 = y0 - dy
		self.canvas.create_line(x0, y0, x1, y1, arrow='last')

	def displayObstacle(self, obs):
		# (x0,y0) = sommet en haut à gauche du rectangle
		# (x1,y1) = sommet en bas à droite du rectangle
		x0 = obs.positionX
		y0 = obs.positionY
		x1 = x0 + obs.width
		y1 = y0 + obs.height
		self.canvas.create_rectangle(x0, y0, x1, y1, fill="grey")