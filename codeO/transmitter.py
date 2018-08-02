from microbit import *
import radio

# can use radio channel

while True:
    i = temperature()
    display.scroll("   First:" + str(i))
    radio.on()
    radio.send("   First:" + str(i))
    radio.off()
    sleep(5000)
    