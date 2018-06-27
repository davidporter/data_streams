import serial

microbit = serial.Serial('/dev/tty.usbmodem1412', 115200)

while True:
    while (microbit.inWaiting()==0):
        pass
    valueRead = microbit.readline()
    print(valueRead)
