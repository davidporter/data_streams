import serial
import time
from tinydb import TinyDB, Query
import openweathermap

db = TinyDB('data_buffer.json')

while True:
    # get from simulator
    value = openweathermap.get_temperature("44236")
    # post it to buffer
    record = {"time": int(time.time()), "id":"outside", "value":value}
    print(record)
    db.insert(record)
    # wait 10 seconds
    time.sleep(60)