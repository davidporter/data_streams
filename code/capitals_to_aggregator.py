import json
import weather
import requests

url = "http://drdelozier.pythonanywhere.com"

def save_to_aggregator(stream,id,time,zip,lat,lon,temp,humidity):
    route = "/save/{stream}/{id}/{time}/{zip}/{lat}/{lon}/{temp}/{humidity}".format(
        stream=stream,
        id=id,
        time=time,
        zip=zip,
        lat=lat,
        lon=lon,
        temp=temp,
        humidity=humidity
    )
    print(route)
    response=requests.get(url + route)
    assert response.status_code == 200 

def send_weather_to_aggregator(id, lat, lon):
    w = weather.get_weather(lat=lat, lon=lon)
    temp = str(w['temp'])
    humidity = str(w['humidity'])
    save_to_aggregator(stream="example",
                       id=id,
                       time="1231414",
                       zip="12345",
                       lat=lat,
                       lon=lon,
                       temp=temp,
                       humidity=humidity)

def send_capital_weather_to_aggregator():
    # load the capitals information
    with open("us_state_capitals.json","r") as f:
        data = json.load(f)
        for key in data:
            item = data[key]
            send_weather_to_aggregator(id=key, lat=item['lat'], lon=item['lon'])

if __name__ == "__main__":
    send_capital_weather_to_aggregator()
