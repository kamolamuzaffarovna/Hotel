from django.urls import path
from .views import BlogListView, BlogDetailView, CommentLike

app_name = 'blog'

urlpatterns = [
    path('list/', BlogListView.as_view(), name='list'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    path('like/<int:bid>/', CommentLike.as_view(), name='likes')
]