from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator

from backend.models import Blog
from core.utils.decorators import AdminOnly


class BlogsView(View):
    template = 'backend/blogs.html'

    @method_decorator(AdminOnly)
    def get(self, request, *args, **kwargs):
        context = {
            'blogs': Blog.objects.all().order_by('-id')
        }
        return render(request, self.template, context)


class CreateUpdateBlockView(View):
    template = 'backend/create_update_blog.html'

    @method_decorator(AdminOnly)
    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})
