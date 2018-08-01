from django.contrib.auth import login
from django.shortcuts import redirect, render

from ..forms import SignupForm

__all__ = (
    'signup',
)


def signup(request):
    """
    회원가입 함수
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.signup()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('index')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'members/signup.html', context)
