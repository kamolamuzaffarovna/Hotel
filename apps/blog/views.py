from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Blog, Tag, Content


class BlogListView(TemplateView):
    template_name = 'blog/blog_list.html'


class DetailView(ListView):
    template_name = 'blog/blog_detail.html'
    context_object_name = 'mixed_lists'

    def get_queryset(self):
        blog = Blog.objects.all()
        tag = Tag.objects.all()
        content = Content.objects.all()
        return list(blog) + list(tag) + list(content)
