import pymongo
import time
import private

from pymongo import MongoClient

import openweathermap

userpass=private.writer_user + ":" + private.writer_pass

#userpass="reader:reader99"

client = MongoClient('mongodb://' + userpass + '@ds121301.mlab.com:21301/data_streams')

db = client.data_streams

weather = db.weather

while True:
    result = openweathermap.get_weather("44240")

    weather_data     = [result]

    results = weather.insert_many(weather_data)
    print(results)
    time.sleep(300)
