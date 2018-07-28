from microbit import *
import radio

while True:
    i = temperature()
    display.scroll("   A:" + str(i))
    radio.on()
    radio.send("   A:" + str(i))
    radio.off()
    sleep(5000)
    