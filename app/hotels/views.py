from django.shortcuts import render

from hotels.models import KoreanHotel, KoreanHotelInfo, KoreanHotelDetail
from region.models import Country, City


def city_list(request):
    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'hotels/cities_list.html', context)


def koreanhotel_list(request, country, city):
    icountry = Country.objects.filter(name=country)[0]
    icity = City.objects.filter(name=city)[0]
    koreanhotels = KoreanHotelInfo.objects.create(country=icountry, city=icity)
    # koreanhotels_list = koreanhotels.get_koreanhotel_list()
    koreanhotels.create_koreanhotel()
    koreanhotels_list = KoreanHotel.objects.filter(city=icity)
    context = {
        'koreanhotels_list': koreanhotels_list,
    }

    return render(request, 'hotels/koreanhotels.html', context)


def koreanhotel_detail(request, country, city, pk):
    try:
        KoreanHotelDetail.objects.get(pk=pk)
    except KoreanHotelDetail.DoesNotExist:
        KoreanHotel.objects.get(pk=pk).create_koreanhotel_detail()

    k_detail = KoreanHotelDetail.objects.get(pk=pk)
    print(k_detail)
    name = k_detail.name
    pictures = k_detail.pictures
    infos = k_detail.infos
    context = {
        'name': name,
        'pictures': pictures,
        'infos' : infos,
        # 'how_to_use_title': infos['how_to_use_title'],
        # 'how_to_use_content': infos['how_to_use_content'],
        # 'cancellation_title': infos['cancellation_title'],
        # 'cancellation_content': infos['cancellation_content'],
    }
    return render(request, 'hotels/koreanhotels_detail.html', context)
