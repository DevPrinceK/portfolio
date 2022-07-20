from django.contrib import admin

from .models import Blog, Category, Work, Client, Subscriber

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Work)
admin.site.register(Client)
admin.site.register(Subscriber)
