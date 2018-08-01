from flask import Flask, render_template, send_from_directory
import json
import private
import weather
import requests

app = Flask(__name__)

@app.route('/')
def get_index():
    return render_template("index.html")

@app.route('/hello/<name>')
def get_hello(name):
    return render_template("hello.html", name=name)

@app.route('/greet/<guests>')
def get_greet(guests):
    guests = guests.split('-')
    return render_template("greet.html", guests=guests)

@app.route('/pizza')
def get_pizza():
    return render_template("pizza.html")

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

@app.route('/map1')
def get_map1():
    return render_template("map1.html",api_key=private.google_key)

@app.route('/map2')
def get_map2():
    # load the capitals information
    with open("us_state_capitals.json","r") as f:
        data = json.load(f)
        data = list(data.values())
    for item in data:
        w = weather.get_weather(lat=item['lat'],lon=item['lon'])
        item['temp'] = str(w['temp'])
        item['humidity'] = str(w['humidity'])
    print(data[0:2])
    return render_template("map2.html",api_key=private.google_key,data=data)

@app.route('/map3')
def get_map3():
    # load the capitals information
    with open("us_state_capitals.json","r") as f:
        data = json.load(f)
        data = list(data.values())
    for item in data:
        w = weather.get_weather(lat=item['lat'],lon=item['lon'])
        temp = int(float(w['temp']) + 0.5)
        item['temp'] = str(temp)
        item['humidity'] = str(w['humidity'])
    #print(data[0:2])
    return render_template("map3.html",api_key=private.google_key,data=data)

@app.route('/map4')
def get_map4():
    url = "http://drdelozier.pythonanywhere.com"
    response = requests.get(url + "/query/example")
    assert response.status_code == 200
    data = list(response.json().values())
    for item in data:
        temp = int(float(item['temp']) + 0.5)
        item['temp'] = str(temp)
    #print(data)
    return render_template("map4.html",api_key=private.google_key,data=data)

@app.route('/mapHumid')
def get_mapHumid():
    url = "http://drdelozier.pythonanywhere.com"
    response = requests.get(url + "/query/example")
    assert response.status_code == 200
    datah = list(response.json().values())
    for item in datah:
        humidity = int(float(item['humidity']))
        item['humidity'] = str(humidity)
    #print(data)
    return render_template("mapHumid.html",api_key=private.google_key,data=datah)

@app.route('/markers1')
def get_markers1():
    return render_template("markers1.html",api_key=private.google_key)

@app.route('/icon/<path:path>')
def get_icon(path):
    return send_from_directory('icon', path)

@app.route('/js/<path:path>')
def get_js(path):
    return send_from_directory('js', path)

@app.route('/static/<path:path>')
def get_static(path):
    return send_from_directory('static', path)

@app.route('/processing2/<int:diameter>')
def get_processing2(diameter=25):
    return render_template("processing2.html",diameter=diameter)

@app.route('/processing3')
def get_processing3():
    with open("us_state_capitals.json","r") as f:
        data = json.load(f)
        #data = list(data.values())
    #print(data)
    states = list(data.keys())
    reds = []
    greens = []
    blues = []
    for state in states:
        item = data[state]
        w = weather.get_weather(lat=item['lat'],lon=item['lon'])
        # print(w)
        temp = float(w['temp'])
        humidity = str(w['humidity'])
        red = int(temp * 5)
        if red < 0: 
            red = 0
        if red > 255:
            red = 255
        reds.append(red)
        greens.append(128)
        blues.append(128) 
    return render_template("processing3.html",
                           states=states, 
                           reds=reds, 
                           greens=greens, 
                           blues=blues)
    f.close()

@app.route('/processingHumid')
def get_processingHumid():
    with open("us_state_capitals.json","r") as f:
        data = json.load(f)
        #data = list(data.values())
    # print(data)
    states = list(data.keys())
    reds = []
    greens = []
    blues = []
    for state in states:
        item = data[state]
        w = weather.get_weather(lat=item['lat'],lon=item['lon'])
        #print(w)
        temp = float(w['temp'])
        humidity = str(w['humidity'])
        blue = int(humidity) *2
        if blue < 0: 
            blue = 0
        if blue > 255:
            blue = 255
        blues.append(blue)
        greens.append(128)
        reds.append(100) 
    return render_template("processingHumid.html",
                           states=states, 
                           reds=reds, 
                           greens=greens, 
                           blues=blues)
