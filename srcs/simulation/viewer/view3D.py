from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from .. import config


def input(key):
	if key == 'escape':
		quit()

class View3D:
    def __init__(self, environment):
        self.window = Ursina() # create a window
        self.environment = environment
        self.arene = Entity(model="quad", color=color.gray, position=Vec3(0,0,0), scale=(environment.width, environment.height, 0))
        editor_camera = EditorCamera() #caméra éditeur d'Ursina
        #cube = Entity(model='cube', color=color.orange, scale=(2,2,2))

        # start running the window
        self.window.run()

    # def update():
    #     print("update")

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
