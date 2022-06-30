from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('', views.LogoutView.as_view(), name='logout'),
]
