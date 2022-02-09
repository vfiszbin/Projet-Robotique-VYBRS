from time import sleep

def moveForward(rob):
	sleep(2)
	rob.changeSpeed(10)
	sleep(5)
	rob.changeSpeed(0)
	rob.changeDir(45)
	sleep(1)
	rob.changeSpeed(30)
	sleep(5)
	rob.changeSpeed(0)
	rob.changeSpeed(-20)
	sleep(3)
	rob.changeSpeed(0)


