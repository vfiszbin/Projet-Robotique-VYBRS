from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ..modele.robot import Robot
from ..modele.obstacle import Obstacle
from .. import config

class View3D:
    def __init__(self,environnement):
        self.window=Ursina()
        self.environment=environment
        self.arene=Entity(model="quad",color=color.gray,scale=(12,12),position=arene_size//2,arene_size//2,-.01)
        camera.position=(field_size//2,-18,-18)
        camera.rotation_x=-56
        self.sky=Sky()
        config.run = False

    def update():



    def displayRobot(self,rob):
        x = rob.positionX
		y = rob.positionY
        rob3D=Entity(model="sphere",color=color.random_color,scale=1)

    def displayObstacle(self,obs):
        x0 = obs.positionX
		y0 = obs.positionY
		x1 = x0 + obs.width
		y1 = y0 + obs.height
        obs3D=entity(collider="box",X=x0,Y=-10,Z=y0,scale=(x1,-10,y1),color=color.colors.random_color())
