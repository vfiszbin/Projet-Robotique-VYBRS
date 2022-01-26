from environment import environment
from robot import robot

env = environment(400,300)
rob = robot(200,140)
env.addObject(rob)
print(env.objects)
rob.changeDir(135)
env.show2D()
env.removeObject(rob)
env.show2D()
