from django.shortcuts import render
from django.views import View

from backend.models import Blog


class BlogsView(View):
    template = 'backend/blogs.html'

    def get(self, request, *args, **kwargs):
        context = {
            'blogs': Blog.objects.all().order_by('-id')
        }
        return render(request, self.template, context)
