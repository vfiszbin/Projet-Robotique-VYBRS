import unittest
from simulation.modele.robot import Robot
from simulation.modele.environment import Environment
from simulation.modele.obstacle import Obstacle
from math import cos,sin,pi
from time import time

# Commande pour lancer les unit_test depuis /srcs :
# python3 -m unittest tests.unit_test -v

class TestRobot(unittest.TestCase):

    def setUp(self):
        self.r1=Robot(2,3)
        self.r2=Robot(10,2)
        self.obs=Obstacle(2,3,2,1)
        self.env=Environment(3,4)
        self.env2=Environment(800,300)
        self.rob = Robot(300,200)
        self.env2.addRob(self.rob)
	    

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

    def test_updateDir(self):
        first_direction=self.r1.dir
        distance = (2 * pi * self.r1.radius_of_wheels ) * (3*pi/ 360) #distance parcourue à partir de l'angle effectué par les roues
        r = self.r1.half_dist_between_wheels #rayon / DOIT REFLETER LA DISTANCE ENTRE LE CENTRE DU ROBOT ET L'UNE DE SES ROUES !!!
        angle_rotated_by_robot = (360 * distance) / (2 * pi * r)
        self.r1.updateDir(3*pi)
        self.assertAlmostEqual(self.r1.dir, (first_direction+angle_rotated_by_robot))

    def test_changeSpeed(self):
        first_speed=self.r1.speed
        self.r1.changeSpeed(50)
        self.assertEqual(self.r1.speed,(first_speed+50))


    def test_deplacerRobot(self):

        first_positionX = self.r1.positionX
        first_positionY = self.r1.positionY
        self.r1.deplacerRobot(70)
        dir = self.r1.dir * pi / 180 #conversion des degrés en radians
        distance = (2 * pi * self.r1.radius_of_wheels) * (70 / 360) #distance parcourue à partir de l'angle effectué par les roues
        dx = distance * cos(dir)
        dy = distance * sin(dir)
        self.assertEqual(self.r1.positionX,first_positionX+dx)
        self.assertEqual(self.r1.positionY,first_positionY-dy)



    def test_update(self):
        """ verifie si la distance  entre le centre du robot est l'une de ses roues et mise a jour
        """
        current_time = time()
        elapsed_time = current_time - self.r1.last_time
        angle_rotated = self.r1.speed * elapsed_time # Angle effectué par les roues = Vitesse (Degrés Par Seconde) * Temps (Secondes)
        first_angle_rotated_left_wheel=self.r1.angle_rotated_left_wheel
        first_angle_rotated_right_wheel=self.r1.angle_rotated_right_wheel
        self.r1.update()
        if self.r1.wheelMode == 1: #roues en mode 1 pour avancer/reculer
            self.assertEqual(self.r1.angle_rotated_left_wheel ,( first_angle_rotated_left_wheel+angle_rotated))
            self.assertEqual(self.r1.angle_rotated_right_wheel ,(first_angle_rotated_right_wheel+angle_rotated))

        elif self.wheelMode == 2: #roues en mode 2 pour tourner
            self.assertEqual(self.r1.angle_rotated_left_wheel ,( first_angle_rotated_left_wheel-angle_rotated))
            self.assertEqual(self.r1.angle_rotated_right_wheel ,( first_angle_rotated_right_wheel+angle_rotated))

        self.r1.last_time = time()
    

    def test_move(self):
        self.r1.move(8,9)
        self.assertEqual(self.r1.positionX,8)
        self.assertEqual(self.r1.positionY,9)

    def test_scalairevectoriel(self):
        resultat=self.r1.scalairevectoriel(2,5,8,3,1,7,4,9)
        k=(2*3-5*8)*(1*9-4*7)
        self.assertAlmostEqual(k,resultat)

    def test_detecteCollision(self):
        k=self.r1.detecteCollision(self.obs)
        self.assertEqual(k,True)

    def test_is_outside_of_the_environment(self):
        k=self.r1.is_outside_of_the_environment(2,3,self.env)
        self.assertEqual(k,False)

    def test_is_inside_an_obstacle_in_the_environment(self):
        self.env.addObject(self.obs)
        k=self.r1.is_inside_an_obstacle_in_the_environment(2, 3, self.env)
        self.assertEqual(k,False)

    def test_getDistance(self):
        k=self.rob.getDistance(self.env2)
        self.assertEqual(k,201)

    if __name__ == '__main__':
        unittest.main()



class TestEnvironment(unittest.TestCase):

    def setUp(self):
        self.env1=Environment(500,300)
        self.rob=Robot(2,3)


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

    def test_addRob(self):
        self.env1.addRob(self.rob)
        self.assertIn(self.rob,self.env1.objects)

    if __name__ == '__main__':
        unittest.main()


class TestObstacle(unittest.TestCase):

    def setUp(self):
        self.ob1=Obstacle()
        self.ob2=Obstacle()

    if __name__ == '__main__':
        unittest.main()
