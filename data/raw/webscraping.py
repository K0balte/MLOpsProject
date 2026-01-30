import requests

url="https://api.open-meteo.com/v1/forecast?latitude=52.52&amp;longitude=13.41&amp;current=temperature_2m,wind_speed_10m&amp;hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

response = requests.get(url)
print(response.text)