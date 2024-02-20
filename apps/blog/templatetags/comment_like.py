from django import template
from apps.blog.models import BlogCommentLike

register = template.Library()

@register.filter(name='user_comment_likes')
def user_comment_likes(comment_id, user_id):
    return BlogCommentLike.objects.filter(blog_id=comment_id, author_id=user_id).exists()