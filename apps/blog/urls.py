from django.urls import path
from .views import BlogListView, BlogDetailView, CommentLike

app_name = 'blog'

urlpatterns = [
    path('list/', BlogListView.as_view(), name='list'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    path('comment-like/<int:comment_id>/', CommentLike.as_view(), name='comment-like'),
    # path('like_parent/<int:pid>/', ParentLike.as_view(), name='like')
]