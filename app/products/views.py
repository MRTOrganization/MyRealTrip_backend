from django.shortcuts import render

from region.models import Country


def product_list(request):
    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'hotels/cities_list.html', context)


def product_detail(request, pk):
    pass
