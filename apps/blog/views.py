from django.shortcuts import render
from django.views.generic import TemplateView


class ListView(TemplateView):
    template_name = 'blog/blog_list.html'


class DetailView(TemplateView):
    template_name = 'blog/blog_detail.html'
