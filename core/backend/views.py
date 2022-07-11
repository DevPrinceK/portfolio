from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from backend.forms import BlogForm

from backend.models import Blog
from core.utils.decorators import AdminOnly


class BlogsView(View):
    template = 'backend/blogs.html'

    # @method_decorator(AdminOnly)
    def get(self, request, *args, **kwargs):
        context = {
            'blogs': Blog.objects.all().order_by('-id')
        }
        return render(request, self.template, context)


class CreateUpdateBlogView(View):
    template = 'backend/create_update_blog.html'

    # @method_decorator(AdminOnly)
    def get(self, request, *args, **kwargs):
        form = BlogForm
        blog_id = request.GET.get('blog_id')
        context = {'form': form}
        if blog_id is not None:
            blog = Blog.objects.filter(id=blog_id).first()
            context['blog'] = blog

        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            try:
                blog.author = request.user if request.user else 'devprincek'
            except ValueError:
                print("COULDN'T ASSIGN AUTHOR")
            finally:
                blog.save()
            return redirect('backend:blogs')
        print(f'ERROS: {form.errors} ')
        return redirect('backend:create_update_blog')


class DeleteBlogPostView(View):
    def get(self, request, *args, **kwargs):
        return redirect('backend:blogs')

    def post(self, request, *args, **kwargs):
        blog_id = request.POST.get('blog_id')
        blog = Blog.objects.filter(id=blog_id).first()
        if blog:
            blog.delete()
            return redirect('backend:blogs')
        print('BLOG DOES NOT EXIST')
        return redirect('backend:blogs')
