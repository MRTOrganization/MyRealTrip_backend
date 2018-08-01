from django.shortcuts import render

__all__ = (
    'mypage',
)

def mypage(request):
    return render(request, 'members/mypage.html')