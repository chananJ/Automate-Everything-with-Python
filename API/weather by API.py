import requests
def get_weather(city,units='metrics',api_key='db831c1ed87460bf76ea41716c5d7d8a'):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    r=requests.get(url)
    contet=r.json()
    with open('weather_data.txt','a') as file:
        for dicty in contet['list']:
            file.write(f"{dicty['dt_txt']},{dicty['main']['temp']},{contet['city']['name']},{dicty['weather'][0]['description']}\n")
    return contet
get_weather(city='Jerusalem')

