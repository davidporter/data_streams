import time
from tinydb import TinyDB, Query
db = TinyDB('data_buffer.json')
query = Query()

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
        print(item)
    time.sleep(15)

