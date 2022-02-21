import unittest
from simulation.modele.robot import Robot
from simulation.modele.environment import Environment
from simulation.modele.obstacle import Obstacle
from math import cos,sin,pi

class TestRobot(unittest.TestCase):

    def setUp(self):
        self.r1=Robot(2,3)
        self.r2=Robot(5,6)

    def test_changeDir(self):
        self.r1.changeDir(5)
        self.assertEqual(self.r1.dir,5)
        self.r1.changeDir(-5)
        self.assertEqual(self.r1.dir,5)
        self.r2.changeDir(10)
        self.assertEqual(self.r2.dir,10)
        self.r2.changeDir(-15)
        self.assertEqual(self.r2.dir, 10)

    def test_deplacerPositionRobotAvant(self):
        dir = self.r1.dir * pi / 180 #conversion des degrés en radians
        self.r1.deplacerPositionRobotAvant(12)
        self.assertAlmostEqual(self.r1.positionX, self.r1.positionX + 12 * cos(dir), 7)
        self.assertAlmostEqual(self.r1.positionY, self.r1.positionY - 12 * cos(dir), 7)

    def test_deplacerPositionRobotArriere(self):
        opposite_dir = (self.r1.dir * pi / 180) + pi #conversion des degrés en radians + on ajoute pi pour obtenir la direction inverse
        positionX_avant=self.r1.positionX
        positionY_avant=self.r1.positionY

        self.r1.deplacerPositionRobotArriere(5)
        self.assertAlmostEqual(self.r1.positionX, positionX_avant + 5* cos(opposite_dir), 7)
        self.assertAlmostEqual(self.r1.positionY, positionY_avant - 5* sin(opposite_dir), 7)
    

    def test_move(self):
        self.r1.move(8,9)
        self.assertEqual(self.r1.positionX,8)
        self.assertEqual(self.r1.positionY,9)


    def test_changeSpeed(self):
        self.r1.changeSpeed(0)
        self.r1.changeSpeed(20)
        self.r2.changeSpeed(10)
        self.r2.changeSpeed(-40)

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
