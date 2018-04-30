import setup
from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions

sensor_pin = 16
RPL.pinMode(sensor_pin,RPL.INPUT)

if RPL.digitalRead(sensor_pin) == 0:
     import RoboPiLib as RPL
     import setup
     RPL.servoWrite(0,0)
     RPL.servoWrite(1,0)
     x = 0

     while True:
          elapsed = time.time() - start
          y = 1
        
     if int(elapsed) != 0:
       y = 2
       while int(elapsed) % 2 == 0:
         RPL.servoWrite(2,2000)
         RPL.servoWrite(1,500)
          
     while True:
          elapsed = time.time() - start
          y = 2
        
        if int(elapsed) != 0:
          y = 4
          while int(elapsed) % 2 == 0:
            RPL.servoWrite(2,0)
            RPL.servoWrite(1,0)
            quit()

