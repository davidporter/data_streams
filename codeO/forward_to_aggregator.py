import time
from tinydb import TinyDB, Query
db = TinyDB('data_buffer.json')
query = Query()

from Adafruit_IO import *
# from private import aio_key
aio_key = "97ab045aa058453b900ba118206a2e31"
aio = Client(aio_key)

def get_current_data():
    data = db.all()
    max = 0
    for item in data:
        if item['time'] > max:
            max = item['time']
    print("Max time = ", max)
    print("# items = ",len(data))
    # delete all items where time <= max
    db.remove(query.time <= max)
    return data

while True:
    data = get_current_data()
    for item in data:
        print('temp', item['value'])
        aio.send('temp', item['value'])
    time.sleep(15)

