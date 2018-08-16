from django.shortcuts import render, redirect

from accom_search.models import AccomSearchInfo


def accom_search_list(request):
    if request.method == 'POST':
        attraction = request.POST['attraction']
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        group_adults = request.POST['group_adults']
        group_children = request.POST['group_children']
        no_rooms = request.POST['no_rooms']
        accom_search = AccomSearchInfo.objects.create(
            attraction=attraction,
            checkin=checkin,
            checkout=checkout,
            group_adults=group_adults,
            group_children=group_children,
            no_rooms=no_rooms,
        )
        return redirect('accom-search-list')
    else:
        accom_searchs = AccomSearchInfo.objects.all()
        context = {
            'accom_searchs': accom_searchs,
        }
    return render(request, 'accom_search/search_list.html', context)


def accom_search_detail(request, pk):
    accom_search_info = AccomSearchInfo.objects.filter(pk=pk)[0]
    accom_search_info.accom_search_url()
    accom_search_details = accom_search_info.accomsearchinfodetail_set.all()
    context = {
        'accom_search_info': accom_search_info,
        'accom_search_details': accom_search_details,
    }
    return render(request, 'accom_search/search_detail.html', context)
