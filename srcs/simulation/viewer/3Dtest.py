from ursina import *

class view3D:
	# create a window
	app = Ursina()

	editor_camera = EditorCamera()
	
	cube = Entity(model='cube', color=color.orange, scale=(2,2,2))

	def input(key):
		if key == 'escape':
			quit()

	# start running the window
	app.run()

view3D()

# # create a window
# app = Ursina()

# editor_camera = EditorCamera()
# cube = Entity(model='cube', color=color.orange, scale=(2,2,2))

# def input(key):
# 	if key == 'escape':
# 		quit()

# # start running the window
# app.run()



