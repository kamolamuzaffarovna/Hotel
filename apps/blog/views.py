from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog, Tag, Content, Comment
from django.contrib import messages


class BlogListView(ListView):
    queryset = Blog.objects.all()
    paginate_by = 2

    def get_tag(self):
        return Tag.objects.all()

    def get_blog(self):
        return Blog.objects.all()[:3]

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tags'] = self.get_tag()
        ctx['blog'] = self.get_blog()

        return ctx


class BlogDetailView(DetailView):
    queryset = Blog.objects.all()
    slug_field = 'slug'

    def get_blog(self):
        return Blog.objects.all()[:3]

    def get_content(self):
        return Content.objects.all()

    def get_comment(self):
        return Comment.objects.filter(blog=self.get_object(), parent__isnull=True)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['blogs'] = self.get_blog()
        ctx['content'] = self.get_content()
        ctx['tags'] = Tag.objects.all()
        ctx['comments'] = self.get_comment()

        return ctx

    def post(self, request, *args, **kwargs):
        message = request.POST.get('message')
        pid = request.GET.get('pid')
        if message:
            instance = self.get_blog()
            user = request.user
            Comment.objects.create(blog_id=instance.id, author_id=user.id, parent_id=pid, message=message)
            return redirect('.')
        messages.error(request, "Comment is empty")
        return redirect('.')

