from flask import Flask, render_template

# Get data
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

# name app same name as file
app = Flask(__name__)

# put in  a route
@app.route('/hello/<name>')
def get_hello(name):
    return render_template("hello.html", name=name)

@app.route('/pizza')
def get_pizza():
    return render_template("pizza.html")

@app.route('/map1')
def get_map1():
    return render_template("map1.html")

@app.route('/map2')
def get_map2():
    return render_template("map2.html")

@app.route('/marker1')
def get_marker1():
    return render_template("marker1.html")
    while True:
        data = get_current_data()

@app.route('/chart')
def get_chart():
    chart_name="Temp and Humidity over Time"
    x_name = "Time"
    y_names = ["Temp","Humidity"]
    data = [
        {'time':'1800',  'temp':28,   'humidity':87},
        {'time':'1900',  'temp':28,   'humidity':84},
        {'time':'2000',  'temp':27,   'humidity':82},
        {'time':'2100',  'temp':25,   'humidity':75},
        {'time':'2200',  'temp':28,   'humidity':87},
        {'time':'2300',  'temp':28,   'humidity':84},
        {'time':'2400',  'temp':27,   'humidity':82},
        {'time':'0000',  'temp':25,   'humidity':75}
    ]
    return render_template("chart.html",
                chart_name=chart_name,
                x_name=x_name, y_names=y_names,
                data=data
                )

@app.route('/barchart')
def get_barchart():
    barchart_name="Temp and Humidity over Time"
    x_name = "Time"
    y_names = ["Temp","Humidity"]
    data = [
        {'time':'1800',  'temp':28,   'humidity':87},
        {'time':'1900',  'temp':28,   'humidity':84},
        {'time':'2000',  'temp':27,   'humidity':82},
        {'time':'2100',  'temp':25,   'humidity':75},
        {'time':'2200',  'temp':28,   'humidity':87},
        {'time':'2300',  'temp':28,   'humidity':84},
        {'time':'2400',  'temp':27,   'humidity':82},
        {'time':'0000',  'temp':25,   'humidity':75}
    ]
    return render_template("barchart.html",
                barchart_name=barchart_name,
                x_name=x_name, y_names=y_names,
                data=data
                )