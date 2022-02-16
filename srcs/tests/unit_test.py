import unittest
from ..simulation.modele.robot import Robot
from ..simulation.modele.environment import Environment
from ..simulation.modele.obstacle import Obstacle
from math import cos,sin,pi
#retourner un repertoire en arrière?
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

    def changeSpeed_test(self):
        self.r1.changeSpeed(0)
        self.r1.changeSpeed(20)
        self.r2.changeSpeed(10)
        self.r2.changeSpeed(-40)

    if __name__ == '__main__':
        main()


class Environment_test(unittest.TestCase):

    def setUp(self):
        self.env1=Environment(500,300)
        self.env2=Environment(600,500)

    def addObject_test(self,obj):
        a=self.env1.addObject()
        b=self.env2.addObject()
        self.assertIn(a,b)

    def test_removeObject(self, obj):
        a=self.env1.removeObject()
        b=self.env2.removeObject()
        self.assertNotIn(obj,a)
        self.assertNotIn(obj,b)

    if __name__ == '__main__':
        main()


class Obstacle_test(unittest.TestCase):

    def setUp(self):
        self.ob1=Obstacle()
        self.ob2=Obstacle()

    if __name__ == '__main__':
        main()
