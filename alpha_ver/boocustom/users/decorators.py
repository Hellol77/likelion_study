from django.shortcuts import redirect
from django.contrib import messages

def login_message_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "접근 권한이 없습니다.")
            return redirect('/')
        return function(request, *args, **kwargs)

    return wrap