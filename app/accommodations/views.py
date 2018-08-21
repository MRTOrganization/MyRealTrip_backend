from django.shortcuts import render

from accommodations.models import PopularHotelInfo
from region.models import Country, City


def country_list(request):
    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'accommodations/country_list.html', context)


def popularhotel_list(request, country, city):
    pcountry = Country.objects.filter(name=country)[0]
    pcity = City.objects.filter(name=city)[0]
    popularhotels = PopularHotelInfo.objects.create(country=pcountry, city=pcity)
    popularhotels_list = popularhotels.get_popularhotel_list()
    popularhotels.create_popularhotel()
    popularcity_list = popularhotels.get_popularcity_list()
    context = {
        'popularhotels_list': popularhotels_list,
        'popularcity_list': popularcity_list,
    }
    return render(request, 'accommodations/popularhotels.html', context)
