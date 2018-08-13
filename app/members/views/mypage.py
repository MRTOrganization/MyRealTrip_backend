from django.shortcuts import render

from wishlist.models import WishList

__all__ = (
    'mypage',
)

def mypage(request):
    wishlist = WishList.objects.all()
    print(wishlist)
    context = {
        'wishlist': wishlist,
    }
    return render(request, 'members/mypage.html', context)
