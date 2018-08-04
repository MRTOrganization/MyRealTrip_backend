from django.shortcuts import render

from region.models import Country


def city_list(request):
    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'products/cities_list.html', context)


def ticket_list(request, city, country):
    print(country, city)
