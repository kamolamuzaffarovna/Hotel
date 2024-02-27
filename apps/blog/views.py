from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Blog, Tag, Content, Comment, BlogCommentLike
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

    # def post(self, request, *args, **kwargs):
    #     message = request.POST.get('message')
    #     pid = request.POST.get('pid', None)
    #     # bid = request.GET.get('bid', None)
    #     if message:
    #         instance = self.get_object()
    #         if instance and instance.id is not None:
    #             user = request.user
    #             Comment.objects.create(blog_id=instance.id, author_id=user.id, parent_id=pid, message=message)
    #             return redirect('.#message')
    #     messages.error(request, "Comment is empty")
    #     return redirect('.')

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login')
        message = request.POST.get('message')
        pid = request.GET.get('pid', None)
        if message:
            instance = self.get_object()
            user = request.user
            Comment.objects.create(blog_id=instance.id, author_id=user.id, parent_id=pid, message=message)
            return redirect(".#message")
        messages.error(request, "Comment is empty")
        return redirect('.')


class CommentLike(View):

    def get(self, request, *args, **kwargs):
        comment_id = self.kwargs.get('comment_id')
        path = request.GET.get('next')

        try:
            existing_like = request.user.comment_like.get(comment_id=comment_id)

            existing_like.delete()
            messages.success(request, "Disliked")

        except BlogCommentLike.DoesNotExist:
            BlogCommentLike.objects.create(author=request.user, comment_id=comment_id)
            messages.success(request, "Liked")

        return redirect(path)

    # def get(self, request, *args, **kwargs):
    #     pid = self.kwargs.get('pid')
    #     path = request.GET.get('next')
    #     if request.user.blogcommentlike_set.filter(comment_id=pid).exists():
    #         request.user.blogcommentlike_set.filter(comment_id=pid).delete()
    #         messages.success(request, "disliked")
    #     else:
    #         BlogCommentLike.objects.create(author_id=request.user.id, comment_id=pid)
    #         messages.success(request, "liked")
    #     return redirect(path)


# class ParentLike(View):
#
#     def get(self, request, *args, **kwargs):
#         pid = self.kwargs.get('pid')
#         path = request.GET.get('end')
#         if request.user.blogparentlike_set.filter(blog_id=pid).exists():
#             request.user.blogparentlike_set.filter(blog_id=pid).delete()
#             messages.success(request, "disliked")
#         else:
#             BlogParentLike.objects.get_or_create(author_id=request.user.id, blog_id=pid)
#             messages.success(request, "liked")
#         return redirect(path)


