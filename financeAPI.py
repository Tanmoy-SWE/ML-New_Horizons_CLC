import pandas
import nasapy

k = "https://api.nasa.gov/planetary/apod?api_key=msb4m1b9I6JPbgsxeaFWKSzZBML1mYhbhHPdsbur"

nasa = nasapy.Nasa(key=k)
apod = nasa.picture_of_the_day(date='2023-01-14', hd=True)
Date_of_release = apod["date"]

print(Date_of_release)