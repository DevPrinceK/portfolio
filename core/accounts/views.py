from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View


class LoginView(View):
    template = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})


class LoginView(View):
    '''Implements login functionality'''
    template = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.is_staff or user.is_superuser:
                return redirect('backend:blogs')
            else:
                logout(request)
                return redirect('accounts:login')
        else:
            return redirect('accounts:login')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:login')
