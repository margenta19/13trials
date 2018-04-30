import setup
from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions

sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)
  
while True:
    elapsed = time.time() - start
    y = 2
    
    if int(elapsed) != 0:
    y = 4
       while int(elapsed) % 2 == 0:
       RPL.servoWrite(2,0)
       RPL.servoWrite(1,0)
       quit()


