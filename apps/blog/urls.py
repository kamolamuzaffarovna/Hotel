from django.urls import path
from .views import BlogListView, DetailView

app_name = 'blog'

urlpatterns = [
    path('list/', BlogListView.as_view(), name='list'),
    path('detail/', DetailView.as_view(), name='detail')
]