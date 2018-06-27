from microbit import *
import radio

radio.on()

while True:
    incoming = radio.receive()
    if not incoming:
        continue
    display.scroll(incoming)
    print(incoming)
    sleep(100)


#import random

#
#while True:
#    if incoming:
#        display.scroll(incoming)
#        print(incoming)
#        i = random.randint(1000000,9999999)
#        print(i)
#        filename = str(i) + ".txt"
#        print(filename)
#        with open(filename,"w") as f:
#            f.write(incoming + "\n")
#            f.close()
#    else:
#        display.scroll("R")
#        sleep(100)