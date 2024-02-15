from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Blog, Tag, Content


class BlogListView(ListView):
    queryset = Blog.objects.all()
    template_name = 'blog/blog_list.html'

    # def get_queryset(self):
    #     tags = Tag.objects.all()
    #
    #     return list(tags)

class DetailView(TemplateView):
    template_name = 'blog/blog_detail.html'

    def get_blog(self):
        return Blog.objects.all()

    def get_content(self):
        return Content.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['blog'] = self.get_blog()
        ctx['content'] = self.get_content()
        ctx['tags'] = Tag.objects.all()

        return ctx

