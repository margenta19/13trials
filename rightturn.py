import setup
from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions
import time
import RoboPiLib as RPL
#time.time- start equal to a value- can have it equal to the end of the program- to find the elapsed time- current time.time
#subtracted by the start time.time is divided- how many leftovers there are when that equals 0 the robot would stop
start = time.time()

x = 6

while True:
    elaptime = (time.time() - start)
    x = 0
    elaptime = int(elaptime)
    if elaptime % 6 == 0:
        RPL.servoWrite(1,0)
        RPL.servoWrite(2,0)
        x = x + 12
    if elaptime % 12 == 0:
        RPL.servoWrite(2,1000)
        RPL.servoWrite(1,250)
        x = x + 6
