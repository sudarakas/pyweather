import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=650cae61864165540abdf179f7ad2d07'
    city = 'Anuradhapura'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    data_weather = []

    for city in cities:

        response = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature':response['main']['temp'],
            'description':response['weather'][0]['description'],
            'icon':response['weather'][0]['icon'],
        }


        data_weather.append(city_weather)

    context = {'data_weather' : data_weather,'form' : form}
    return render(request, 'pyweather/index.html',context)
