from django.contrib import admin

from .models import Blog, Category, Tag, Work, Client

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Work)
admin.site.register(Client)
