import unittest
from simulation.modele.robot import Robot 
from math import cos,sin,pi

class robot_test(unittest.TestCase):

    def setUp(self):
        self.r1=Robot(self,2,3)
        self.r2=Robot(self,5,6)

    def changeDir_test(self):
        self.r1.changeDir(5)
        self.assertEqual(self.r1.dir,5)
        self.r1.changeDir(-5)
        self.assertEqual(self.r1.dir,5)
        self.r2.changeDir(10)
        self.assertEqual(self.r2.dir,10)
        self.r2.changeDir(-15)
        self.assertEqual(self.r2.dir,10)
        
    def deplacerPositionRobotAvant(self):
        self.r1.deplacerPositionRobotAvant(12)
        self.assertEqual(self.r1.positionX,self.positionX+12 * cos(dir))
