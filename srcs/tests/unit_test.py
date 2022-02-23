import unittest
from simulation.modele.robot import Robot
from simulation.modele.environment import Environment
from simulation.modele.obstacle import Obstacle
from math import cos,sin,pi

class TestRobot(unittest.TestCase):

    def setUp(self):
        self.r1=Robot(2,3)
        self.r2=Robot(10,2)

    def test_changeDir(self):
        self.r1.changeDir(5)
        self.assertEqual(self.r1.dir,5)
        self.r1.changeDir(-5)
        self.assertEqual(self.r1.dir,-5)
        self.r2.changeDir(10)
        self.assertEqual(self.r2.dir,10)
        self.r2.changeDir(-15)
        self.assertEqual(self.r2.dir, -15)

    def test_deplacerRobot(self):
        dir = self.r1.dir * pi / 180 #conversion des degrés en radians
        self.r1.deplacerRobot(12)
        self.assertAlmostEqual(self.r1.positionX, self.r1.positionX + 12 * cos(dir), 7)
        self.assertAlmostEqual(self.r1.positionY, self.r1.positionY - 12 * cos(dir), 7)


    def test_move(self):
        self.r1.move(8,9)
        self.assertEqual(self.r1.positionX,8)
        self.assertEqual(self.r1.positionY,9)


    def test_changeSpeed(self):
        self.r1.changeSpeed(0)
        self.r1.changeSpeed(20)
        self.r2.changeSpeed(10)
        self.r2.changeSpeed(-40)

    def test_detecteCollision(self):
        test_obj = Obstacle(10,50,100,30)
        self.r1.detecteCollision(test_obj)

    def test_changeWheelMode(self):
        self.r1.changeWheelMode(2)
        self.assertEqual(self.r1.wheelMode,2)

    if __name__ == '__main__':
        unittest.main()



class TestEnvironment(unittest.TestCase):

    def setUp(self):
        self.env1=Environment(500,300)


    def test_addObject(self):
        test_obj = Obstacle(10,50,100,30)
        self.env1.addObject(test_obj)
        self.assertIn(test_obj, self.env1.objects)

    def test_removeObject(self):
        test_obj = Obstacle(10,50,100,30)
        self.env1.addObject(test_obj)
        self.assertIn(test_obj, self.env1.objects)
        self.env1.removeObject(test_obj)
        self.assertNotIn(test_obj, self.env1.objects)

    if __name__ == '__main__':
        unittest.main()


class TestObstacle(unittest.TestCase):

    def setUp(self):
        self.ob1=Obstacle()
        self.ob2=Obstacle()

    if __name__ == '__main__':
        unittest.main()
