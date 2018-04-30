    while True:
        elapsed = time.time() - start
        y = 2
        
        if int(elapsed) != 0:
          y = 4
          while int(elapsed) % 2 == 0:
            RPL.servoWrite(2,0)
            RPL.servoWrite(1,0)
            quit()


