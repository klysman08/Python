'''Get weather fir a city with weatherbit.io'''
def get_weather(city):
    import requests
    url = f'https://api.weatherbit.io/v2.0/current?city={city}&key=d8a8c7a9d9f24c8f9a9a8b7f7e0a0e2a'
    response = requests.get(url)
    return response.json()

print(get_weather('São Paulo'))