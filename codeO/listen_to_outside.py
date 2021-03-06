import serial
import time
from tinydb import TinyDB, Query
import openweathermap

db = TinyDB('data_buffer.json')

while True:
    # get from simulator
    # denver seems nice
    value = openweathermap.get_temperature("41.275150", "-81.419015")
    # post it to buffer
    record = {"time": int(time.time()), "id":"outside", "value":value}
    print(record)
    db.insert(record)
    # wait 10 seconds
    time.sleep(60*30)