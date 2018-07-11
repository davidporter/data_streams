import serial
import time
from tinydb import TinyDB, Query
import openweathermap

db = TinyDB('data_buffer.json')

while True:
    # get from simulator
    # denver seems nice
    value = openweathermap.get_temperature("39.7392", "104.9903")
    # post it to buffer
    record = {"time": int(time.time()), "id":"dbp.micro", "value":value}
    print(record)
    db.insert(record)
    # wait 10 seconds
    time.sleep(10)