from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog/', views.BlogView.as_view(), name='blog'),
]
