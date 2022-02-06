from tkinter import Tk, Canvas
from math import cos, sin, pi
from ..objects.robot import Robot
from ..objects.obstacle import Obstacle
from ..updater.updateSimulation import updateSimulation
import threading


def show2D(env, rob):
	'''
	L'affichage graphique avec tkinter requiert de lancer une mainloop() qui va bloquer l'execution de toute autre instructions (c'est équivalent à
	une boucle while infinie). Pour continuer à executer d'autres instructions que l'affichage graphique on lance updateSimulation()
	dans un thread secondaire qui s'execute en parallèle de l'affichage graphique.
	'''
	thread = threading.Thread(target=updateSimulation,args=(env,rob))
	# thread.setDaemon(True) #pour que le thread meurt lorsque le main thread se termine
	thread.start()
	graphicalRepresentation(env)


class graphicalRepresentation:
	def __init__(self, environment):
		self.window = Tk()
		self.window.title("Environnement")
		self.environment = environment
		self.canvas = Canvas(self.window, height=environment.height, width=environment.width)
		self.canvas.pack()

		self.window.after(1000, self.update) #executera update() dans 1000 ms

		self.window.mainloop() # bloque le main thread

	def update(self):
		'''
		Une fois l'affichage graphique lancé en appelant mainloop(), l'execution de code est bloquée dans le main thread,
		on utilise donc after() qui va appeler cette fonction toutes les x ms pour mettre à jour l'affichage graphique
		'''
		self.canvas.delete("all") # efface tous les objets déjà affichés, cela évite de créer des doubles
		for obj in self.environment.objects: #représentation visuelle de chaque objet ajouté à l'environnement
			if isinstance(obj, Robot):
				#Création d'un cerle pour représenter la position du robot
				r = 3 #rayon
				x = obj.positionX
				y = obj.positionY
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
				dir = obj.dir * pi / 180 #conversion des degrés en radians
				dx = len_arrow * cos(dir)
				dy = len_arrow * sin(dir)
				x1 = x0 + dx
				y1 = y0 - dy
				self.canvas.create_line(x0, y0, x1, y1, arrow='last')

			elif isinstance(obj, Obstacle):
				# (x0,y0) = sommet en haut à gauche du rectangle
				# (x1,y1) = sommet en bas à droite du rectangle
				x0 = obj.positionX
				y0 = obj.positionY
				x1 = x0 + obj.width
				y1 = y0 + obj.height
				self.canvas.create_rectangle(x0, y0, x1, y1, fill="grey")

		self.window.after(1000, self.update) # update() se rappelle elle même toutes les 1000 ms
