from microbit import *


i = 1

while True:    
    display.scroll(str(i))
    with open("data.txt", "a") as f:
        f.write(str(i) + "\n")
        f.close()
    i = i + 1
    sleep(5000)
    
    