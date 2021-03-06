import time
from tinydb import TinyDB, Query
import pymongo
from pymongo import MongoClient

# setup TinyDB data buffer
db = TinyDB('data_buffer.json')
query = Query()

# setup MongoDB aggregator
userpass="davidporter:1234567a"
# mongodb://<dbuser>:<dbpassword>@ds121311.mlab.com:21311/data_streams
mongo_client = MongoClient('mongodb://' + userpass + '@ds121311.mlab.com:21311/data_streams')
mongo_db = mongo_client.data_streams
mongo_data = mongo_db.data
print(str(mongo_client))

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
    if len(data) > 0:
        for item in data:
            print(item)
        results = mongo_data.insert_many(data)
        print(results.inserted_ids)
    time.sleep(15)

