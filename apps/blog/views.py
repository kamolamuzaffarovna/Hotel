from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog, Tag, Content


class BlogListView(ListView):
    queryset = Blog.objects.all()


class BlogDetailView(DetailView):
    queryset = Blog.objects.all()
    slug_field = 'slug'

    def get_blog(self):
        return Blog.objects.all()

    def get_content(self):
        return Content.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['blogs'] = self.get_blog()
        ctx['content'] = self.get_content()
        ctx['tags'] = Tag.objects.all()

        return ctx

