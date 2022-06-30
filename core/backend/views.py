from django.shortcuts import render
from django.views import View


class BlogsView(View):
    template = 'backend/blogs.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template, context)
