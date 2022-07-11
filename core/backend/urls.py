from django.urls import path
from . import views

app_name = 'backend'
urlpatterns = [
    path('', views.BlogsView.as_view(), name='blogs'),
    path('create-update-blog/', views.CreateUpdateBlogView.as_view(), name='create_update_blog'),  # noqa
    path('delete-blog/', views.DeleteBlogPostView.as_view(), name='delete_blog'),

]
