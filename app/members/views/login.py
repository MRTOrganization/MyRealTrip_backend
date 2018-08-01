from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.shortcuts import redirect, render

__all__ = (
    'login_view',
)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # next = request.GET['next']
            #
            # if next:
            #     return redirect(next)
            return redirect('index')
        else:
            return redirect('members:login')
    else:
        return render(request, 'members/login.html')
