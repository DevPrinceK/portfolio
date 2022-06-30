from django.shortcuts import render
from django.views import View

from backend.models import Blog


class IndexView(View):
    template = 'website/index.html'

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        context = {
            'blogs': blogs,
        }
        return render(request, self.template, context)


class BlogView(View):
    template = 'website/blog.html'

    def get(self, request, *args, **kwargs):
        blog_id = request.GET.get('blog_id')
        blog = Blog.objects.filter(id=blog_id).first()

        tags = blog.tags.all()

        context = {
            'blog': blog,
            'tags': tags,
        }
        return render(request, self.template, context)
