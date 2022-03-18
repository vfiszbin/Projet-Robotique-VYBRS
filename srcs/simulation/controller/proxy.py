class AngleRotatedSimu:
	def __init__(self, rob):
		self.rob = rob

	def getAngleRotatedLeft(self):
		return self.rob.angle_rotated_left_wheel

	def getAngleRotatedRight(self):
		return self.rob.angle_rotated_right_wheel

class AngleRotatedReal:
	def __init__(self, rob):
		self.rob = rob

	def getAngleRotatedLeft(self):
		l_pos, r_pos = self.rob.get_motor_position()
		return l_pos

	def getAngleRotatedRight(self):
		l_pos, r_pos = self.rob.get_motor_position()
		return r_pos