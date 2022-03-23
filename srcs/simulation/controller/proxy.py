class ProxySimu:
	def __init__(self, rob):
		self.rob = rob

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

class ProxyReal:
	def __init__(self, rob):
		self.rob = rob
		self.wheelMode = 1

	def getAngleRotatedLeft(self):
		l_pos, r_pos = self.rob.get_motor_position()
		return l_pos

	def getAngleRotatedRight(self):
		l_pos, r_pos = self.rob.get_motor_position()
		return r_pos
		
	def resetAngleRotated(self):
		#lit la position des moteurs
		l_pos, r_pos = self.robot.get_motor_position()
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

