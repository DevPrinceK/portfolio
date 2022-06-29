from django.shortcuts import render
from django.views import View


class IndexView(View):
    template = 'website/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template, context)


class BlogView(View):
    template = 'website/blog.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template, context)
