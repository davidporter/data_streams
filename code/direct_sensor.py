from microbit import *

while True:
    i = temperature()
    display.scroll(" direct:" + str(i))
    print(" direct:" + str(i))
    sleep(5000)
    