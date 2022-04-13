from ursina import *

class view3D:
	def __init__(self):
		# create a window
		app = Ursina()
		editor_camera = EditorCamera()

		cube = Entity(model='cube', color=color.orange, scale=(2,2,2))

		# start running the window
		app.run()


def input(key):
	if key == 'escape':
		quit()


def start():
	view3D()

start()

# # create a window
# app = Ursina()

# editor_camera = EditorCamera()
# cube = Entity(model='cube', color=color.orange, scale=(2,2,2))

# def input(key):
# 	if key == 'escape':
# 		quit()

# # start running the window
# app.run()



