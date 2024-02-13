from django.urls import path
from .views import ListView, DetailView

app_name = 'blog'

urlpatterns = [
    path('list/', ListView.as_view(), name='list'),
    path('detail/', DetailView.as_view(), name='detail')
]