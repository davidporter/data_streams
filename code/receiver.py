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