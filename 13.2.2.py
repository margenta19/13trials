import setup
from setup import RPL
import post_to_web as PTW

sensor_pin = 17
RPL.pinMode(sensor_pin, RPL.INPUT)

while True:
  PTW.state['d1'] = RPL.digitalRead(sensor_pin)
  PTW.post()

  if RPL.digitalRead(sensor_pin) == 1:
     import RoboPiLib as RPL
     import setup
     RPL.servoWrite(1,500)
     RPL.servoWrite(2,2000)
    
  if RPL.digitalRead(sensor_pin) == 0:
     import setup
     from setup import RPL
     import post_to_web as PTW # see post_to_web.py for instructions
     import time
     import RoboPiLib as RPL

     start = time.time()

     x = 1

     elaptime = (time.time() - start)
     x = 0
     elaptime = int(elaptime)
       if elaptime % 1 == 0:
          RPL.servoWrite(1,0)
          RPL.servoWrite(2,0)
          x = x + 2
       if elaptime % 2 == 0:
          RPL.servoWrite(2,1000)
          RPL.servoWrite(1,250)
          x = x + 1
