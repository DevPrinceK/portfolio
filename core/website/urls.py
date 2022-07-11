from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blogs/', views.BlogsView.as_view(), name='blogs'),
    path('blog/<str:blog_id>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('services/', views.ServicesView.as_view(), name='services'),
]
