from django.urls import path
from . import views

app_name = 'backend'
urlpatterns = [
    path('', views.BlogsView.as_view(), name='blogs'),
]
