import serial
import time
from tinydb import TinyDB, Query
db = TinyDB('data_buffer.json')
#table = db.table('table_name', cache_size=30)
db.purge()

microbit = serial.Serial('/dev/tty.usbmodem1412', 115200)

while True:
    while (microbit.inWaiting()==0):
        pass
    value = microbit.readline()
    # print(value)
    if not value:
        continue
    value = value.decode("utf-8") # convert from bytes to string type
    value = value.strip()
    # print(value)
    if not (":" in value):
        continue
    id, value = value.split(":")
    if len(id) == 0:
        continue
    if len(value) == 0:
        continue    
    # print(id, value)
    record = {"time": int(time.time()), "id":id, "value":value}
    print(record)
    db.insert(record)
