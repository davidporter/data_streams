from flask import Flask, jsonify
import json
from tinydb import TinyDB, Query

db = TinyDB('aggregator_buffer.json')
query = Query()

app = Flask(__name__)

        # 'zip':zip,
        # 'time':data['dt'],
        # 'lat':data['coord']['lat'],
        # 'lon':data['coord']['lon'],
        # 'temp':int((data['main']['temp'] - 273.15) * 100)/100.0,
        # 'humidity':data['main']['humidity']

@app.route('/save/<stream>/<id>/<time>/<zip>/<lat>/<lon>/<temp>/<humidity>')
def get_save(stream,id,time,zip,lat,lon,temp,humidity):
    record = {
        "stream":stream,
        "id" : id,
        "zip" : zip,
        "time" : time,
        "lat" : lat,
        "lon" : lon,
        "temp" : temp,
        "humidity" : humidity
    }
    db.insert(record)
    return jsonify(record)

@app.route("/query/<stream>")
def get_query(stream):
    data = db.all()
    data = [item for item in data if item['stream'] == stream]
    d = {}
    for item in data:
        d[item['id']] = item
    return jsonify(d)

@app.route("/clear/<stream>")
def get_clear(stream):
    db.remove(query.stream == stream)
    return jsonify({})
