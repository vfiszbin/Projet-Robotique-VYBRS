class ProxySimu:
	def __init__(self, rob, env):
		self.rob = rob
		self.env = env

	def getAngleRotatedLeft(self):
		return self.rob.angle_rotated_left_wheel

	def getAngleRotatedRight(self):
		return self.rob.angle_rotated_right_wheel

	def resetAngleRotated(self):
		self.rob.angle_rotated_left_wheel = 0
		self.rob.angle_rotated_right_wheel = 0

	def setSpeed(self, speed):
		self.rob.changeSpeed(speed)

	def setWheelMode(self, mode):
		self.rob.changeWheelMode(mode)

	def getRadius(self) :
		return self.rob.radius_of_wheels

	def getHalfDistBetweenWheels(self):
		return self.rob.half_dist_between_wheels

	def getDistance(self):
		return self.rob.getDistance(self.env)

class ProxyReal:
	def __init__(self, rob):
		self.rob = rob
		self.wheelMode = 1
		
		print("WHEEL_DIAMETER=")
		print(self.rob.WHEEL_DIAMETER)

	def getAngleRotatedLeft(self):
		l_pos, r_pos = self.rob.get_motor_position()
		return l_pos

	def getAngleRotatedRight(self):
		l_pos, r_pos = self.rob.get_motor_position()
		return r_pos
		
	def resetAngleRotated(self):
		#lit la position des moteurs
		l_pos, r_pos = self.rob.get_motor_position()
		# remet à 0 l'offset du moteur gauche et droit
		self.rob.offset_motor_encoder(self.rob.MOTOR_LEFT, l_pos)
		self.rob.offset_motor_encoder(self.rob.MOTOR_RIGHT, r_pos)

	def setSpeed(self, speed):
		if self.wheelMode == 1:
			self.rob.set_motor_dps(self.rob.MOTOR_LEFT + self.rob.MOTOR_RIGHT, speed)

		elif self.wheelMode == 2:
			self.rob.set_motor_dps(self.rob.MOTOR_LEFT, -speed)
			self.rob.set_motor_dps(self.rob.MOTOR_RIGHT, speed)

	def setWheelMode(self, mode):
		self.wheelMode = mode

	def getRadius(self) :
		return self.rob.WHEEL_DIAMETER / 2 
	
	def getHalfDistBetweenWheels(self):
		return self.rob.WHEEL_BASE_WIDTH / 2 

	def getDistance(self):
		return self.rob.get_distance()

