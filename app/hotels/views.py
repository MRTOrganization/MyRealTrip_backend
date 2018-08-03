from django.shortcuts import render

from hotels.models import KoreanHotel, KoreanHotelInfo
from region.models import Country, City


def city_list(request):
    countries = Country.objects.all()
    context = {
        'countries':countries,
    }
    return render(request, 'hotels/cities_list.html', context)

def koreanhotel_list(request, country, city):
    print(country, city)
    icountry = Country.objects.filter(name=country)[0]
    icity = City.objects.filter(name=city)[0]
    koreanhotels = KoreanHotelInfo.objects.create(country=icountry, city=icity)
    koreanhotels_list = koreanhotels.get_koreanhotel_list()
    context = {
        'koreanhotels_list':koreanhotels_list,
    }
    print(koreanhotels_list)
    return render(request, 'hotels/koreanhotels.html', context)
