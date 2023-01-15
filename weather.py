import requests
import math
city =  'New York'
API_key = '464180b8505f4807a4494e41590e7e67'
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

response = requests.get(url).json()

temper = response['main']['temp']
temp = math.floor((temper * 1.8) - 459.67)  # Convert to °F

feels_like = response['main']['feels_like']
feels_like = math.floor((feels_like * 1.8) - 459.67)  # Convert to °F

humidity = response['main']['humidity']
print(temp)

