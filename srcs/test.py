from robot2I013 import Robot2I013 as Robot
from time import sleep
from PIL import Image

rob = Robot()
sleep(5)
img = rob.get_image()
# sleep(5)
Image.fromarray(img).save("qwdertf_bow.jpg", "JPEG")

print(type(img))
print(img.shape)
print(img)




# from picamera import PiCamera
# from time import sleep

# camera = PiCamera()
# camera.start_preview()
# sleep(5)
# camera.capture('test_picture.jpg')
# camera.stop_preview()



# import time
# import picamera
# import numpy as np

# with picamera.PiCamera() as camera:
#     camera.resolution = (320, 240)
#     camera.framerate = 24
#     time.sleep(2)
#     output = np.empty((240, 320, 3), dtype=np.uint8)
#     camera.capture(output, 'rgb')

# print(output.shape)
# im = Image.fromarray(output)
# im.save("test_img.jpg")