from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
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

    def get_blogs(self):
        return Blog.objects.all()

    def get_comment(self):
        return Comment.objects.filter(blog=self.get_object(), parent__isnull=True).order_by('-id')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['blogs'] = self.get_blog()
        ctx['content'] = self.get_content()
        ctx['tags'] = Tag.objects.all()
        ctx['comments'] = self.get_comment()

        return ctx

    def post(self, request, *args, **kwargs):
        message = request.POST.get('message')
        pid = request.GET.get('pid', None)
        if message:
            instance = self.get_object()
            if instance and instance.id is not None:
                user = request.user
                Comment.objects.create(blog_id=instance.id, author_id=user.id, parent_id=pid, message=message)
                return redirect('.#message')
        messages.error(request, "Comment is empty")
        return redirect('.')


class BlogCommentLike(View):
    def get(self, request, *args, **kwargs):
        bid = self.kwargs.get('bid')
        path = request.GET.get('next')
        if request.user.blogcommentlike_set.filter(blog_id=bid).exists():
            request.user.blogcommentlike_set.filter(blog_id=bid).delete()
            messages.success(request, "disliked")
        else:
            Blog.objects.create(author_id=request.user.id, blog_id=bid)
            messages.success(request, "liked")
        return redirect('.')

