import setup 
from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions
import RoboPiLib as RPL

sensor_pin = 17
RPL.pinMode(sensor_pin, RPL.INPUT)

while True:
  PTW.state['d1'] = RPL.digitalRead(sensor_pin)
  PTW.post()
  
  
if RPL.digitalRead(sensor_pin) == 1:
  import RoboPiLib as RPL
  import setup
  import time
  x = 1
  elaptime = (time.time() - start)
  RPL.servowrite(1,500)
  RPL.servowrite(2,2000)
