from django.shortcuts import render

from hotels.crawler import KoreanHotelDetail
from hotels.models import KoreanHotel, KoreanHotelInfo
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
    koreanhotel = KoreanHotel.objects.get(pk=pk)
    koreanhotel_detail = KoreanHotelDetail(
        city=city,
        country=country,
        thumbnail=koreanhotel.thumbnail,
        name=koreanhotel.name,
        city_name= koreanhotel.city.name,
        comments=koreanhotel.comments,
        price=koreanhotel.price,
        detail_url=koreanhotel.detail_url,
    )
    result = koreanhotel_detail.search_koreanhotel_detail()
    name = result.name
    pictures = result.picture_list
    infos = result.info_dict
    context = {
        'name':name,
        'pictures':pictures,
        'how_to_use_title':infos['how_to_use_title'],
        'how_to_use_content':infos['how_to_use_content'],
        'cancellation_title':infos['cancellation_title'],
        'cancellation_content':infos['cancellation_content'],
    }
    return render(request, 'hotels/koreanhotels_detail.html', context)


