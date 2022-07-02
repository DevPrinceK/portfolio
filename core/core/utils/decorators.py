from django.shortcuts import redirect

class AdminOnly(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return self.original_function(request, *args, **kwargs)
        return redirect('accounts:login')