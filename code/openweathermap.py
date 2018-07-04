import requests

def get_temperature(zip):
    key = "ee2c34782a8ad4b9609038f7239b45ac"
    q = "http://api.openweathermap.org/data/2.5/weather?zip={z},us&APPID={k}".format(z=zip, k=key)
    response = requests.get(q)
    data = response.json()
    temp = (data['main']['temp'] - 273.15)  # * 9 / 5 + 32
    return int(temp * 100)/100.0 

if __name__ == "__main__":
    print(get_temperature("44281"))