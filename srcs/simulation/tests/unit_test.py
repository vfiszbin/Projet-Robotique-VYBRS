import unittest
from math import cos,sin,pi

class robot_test(unittest.TestCase):
    def changeDir_test(self,dir):
        self.assertGreaterEqual(dir,0)
        self.assertLessEqual(dir,360)

    def deplacerPositionRobotAvant(self,distance):
        self.dir * pi / 180 #conversion des degrés en radians
        dx = distance * cos(dir)
        dy = distance * sin(dir)
        self.assertEqual(self.positionX,self.positionX+dx)