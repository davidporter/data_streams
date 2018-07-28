import requests

# weather?lat=35&lon=139
def get_temperature(latitude, longitude):
    key = "3fb93918c9b5dfd7879675897281195d"
    q = "http://api.openweathermap.org/data/2.5/weather?lat={a}&lon={o}&appid={k}".format(a=latitude, o=longitude, k=key)
    response = requests.get(q)
    data = response.json()
    print("data = "+str(data))
    temp = (data['main']['temp'] - 273.15)  # * 9 / 5 + 32
    return int(temp * 100)/100.0 

if __name__ == "__main__":
    print(get_temperature("35.00", "-106.00"))