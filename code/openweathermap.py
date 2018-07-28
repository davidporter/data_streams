import requests
import private

def get_temperature(zip):
    key = private.owm_key
    q = "http://api.openweathermap.org/data/2.5/weather?zip={z},us&APPID={k}".format(z=zip, k=key)
    response = requests.get(q)
    data = response.json()
    temp = (data['main']['temp'] - 273.15)  # * 9 / 5 + 32
    return int(temp * 100)/100.0 

def get_weather(zip):
    key = private.owm_key
    q = "http://api.openweathermap.org/data/2.5/weather?zip={z},us&APPID={k}".format(z=zip, k=key)
    response = requests.get(q)
    data = response.json()
    time = data['dt']
    temp = (data['main']['temp'] - 273.15)  # * 9 / 5 + 32
    temp = int(temp * 100)/100.0 
    lon = data['coord']['lon']
    lat = data['coord']['lat']
    humidity = data['main']['humidity']
    # print(data)
    result={
        'zip':zip,
        'time':time,
        'lat':lat,
        'lon':lon,
        'temp':temp,
        'humidity':humidity
    }
    return(result)

if __name__ == "__main__":
    print(get_weather("44240"))