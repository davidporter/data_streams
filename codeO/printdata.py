from microbit import *

while True:
    
    with open("data2.txt","r") as f:
        line = f.readline()
        display.scroll(line)
        sleep(1000)
    
    