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
    import RoboPiLib as RPL
    import setup
    RPL.servoWrite(2,500)
    RPL.servoWrite(1,2000)
