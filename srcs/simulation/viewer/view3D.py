from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from .. import config
from threading import Thread
from time import sleep
from ..modele.robot import Robot
from ..modele.obstacle import Obstacle
from math import cos, sin, pi

UPDATE_FREQUENCY = 0.1 #en secondes

def input(key):
	if key == 'escape':
		quit()

class View3D:
    def __init__(self, environment):
        self.app = Ursina() # create a window
        self.environment = environment
        self.arene = Entity(model="quad", color=color.gray, origin=(-0.5,0.5), scale=(environment.width, environment.height, 0))
        editor_camera = EditorCamera() #caméra éditeur d'Ursina
        self.entity_of_object = dict() #L'objet est identifié par son id()
        editor_camera.position = (environment.width / 2, -(environment.height / 2), -100)


        #démarre le thread d'update de l'affichage
        update_thread = Thread(target=self.update, args=())
        update_thread.start()

        # start running the window
        self.app.run()

    def update(self):
        while(True):
            for obj in self.environment.objects: #représentation visuelle de chaque objet ajoutée/maj dans l'environnement
                if isinstance(obj, Robot):
                    self.displayRobot(obj)

                elif isinstance(obj, Obstacle):
                	self.displayObstacle(obj)

            sleep(UPDATE_FREQUENCY)


    def displayRobot(self, rob):
        if (id(rob) not in self.entity_of_object): #si l'entité pour cet objet n'existe pas encore, la créée
            robot_entity = Entity(model='sphere', color=color.orange, origin=(-0.5,0.5), scale=(10,10,10))
            
            #Création d'une flèche représentant la direction du robot
            arrow_entity = Entity(model='cube', color=color.red, origin=(-0.5,0.5), scale=(2,15,2))

            self.entity_of_object[id(rob)] = (robot_entity, arrow_entity)

        x = rob.positionX
        y = rob.positionY
        self.entity_of_object[id(rob)][0].position = (x,-y,0)

        #Maj de la direction
        self.entity_of_object[id(rob)][1].position = (x + 5, -(y + 5), 0)
        self.entity_of_object[id(rob)][1].rotation_z = -(rob.dir + 90)


    def displayObstacle(self,obs):
        if (id(obs) not in self.entity_of_object): #si l'entité pour cet objet n'existe pas encore, la créée
            obs_entity = Entity(model='cube', color=color.blue, origin=(-0.5,0.5), scale=(obs.width, obs.height, 30))
            self.entity_of_object[id(obs)] = obs_entity
            print(id(obs))

        x = obs.positionX
        y = obs.positionY
        self.entity_of_object[id(obs)].position = (x,-y,0)
