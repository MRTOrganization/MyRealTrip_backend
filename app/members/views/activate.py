from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from members.tokens import account_activation_token

__all__ = (
    'activate',
)

User = get_user_model()


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'members/user_active_complete.html')
    else:
        return HttpResponse('Activation link is invalid!')
