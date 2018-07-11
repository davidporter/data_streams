import serial
import time
from tinydb import TinyDB, Query
import openweathermap

db = TinyDB('data_buffer.json')

while True:
    # get from simulator
    # charleston sc seems like a nice place to work
    value = openweathermap.get_temperature("32.7765", "79.9311")
    # post it to buffer
    record = {"time": int(time.time()), "id":"dbp.work", "value":value}
    print(record)
    db.insert(record)
    # wait 10 seconds
    time.sleep(10)