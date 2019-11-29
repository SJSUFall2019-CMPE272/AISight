from picamera import PiCamera
from time import sleep
import time
#from captionbot import CaptionBot

#c=CaptionBot()

camera = PiCamera()
while(True):
        camera.start_preview()
        sleep(1)
        camera.capture('1.jpg')
 