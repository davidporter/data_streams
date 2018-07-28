import pymongo

from pymongo import MongoClient

userpass="streams:streams111"

client = MongoClient('mongodb://' + userpass + '@ds121301.mlab.com:21301/data_streams')

db = client.data_streams

measurements = db.measurements

measurement_data = [{"time":123141422, "id":"alpha", "value":"113"},
                    {"time":123141442, "id":"alpha", "value":"133"}]

results = measurements.insert_many(measurement_data)
print(results)