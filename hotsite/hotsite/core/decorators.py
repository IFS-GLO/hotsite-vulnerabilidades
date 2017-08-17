from django.http.response import HttpResponseRedirect
from django.urls import reverse


def login_required(function):
    def wrapper(request, *args, **kwargs):
        user = request.user

        if not user.id:
            return HttpResponseRedirect(reverse('panel:login'))
        else:
            return function(request, *args, **kwargs)

    return wrapper
