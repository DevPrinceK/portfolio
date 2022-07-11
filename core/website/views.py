from django.shortcuts import render, redirect
from django.views import View
from backend.forms import ContactForm

from backend.models import Blog


class IndexView(View):
    template = 'website/index.html'

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all().order_by(
            '-id')[:3] if Blog.objects.all() else {}
        context = {'blogs': blogs}

        return render(request, self.template, context)


class AboutView(View):
    template = 'website/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})


class BlogsView(View):
    template = 'website/blogs.html'

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all().order_by('-id')
        return render(request, self.template, {'blogs': blogs})


class BlogDetailView(View):
    template = 'website/blog_details.html'

    def get(self, request, blog_id, *args, **kwargs):
        blog = Blog.objects.filter(id=blog_id).first()
        related_blogs = Blog.objects.filter(
            category=blog.category).order_by('-id')
        return render(request, self.template, {'blog': blog, 'related_blogs': related_blogs})


class ContactView(View):
    template = 'website/contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:index')
        print(f'form.errors: {form.errors}')
        return redirect('website:index')


class ProjectsView(View):
    template = 'website/projects.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})


class ResumeView(View):
    template = 'website/resume.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})


class ServicesView(View):
    template = 'website/services.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})
