from django.urls import path
from .views import RoomListView, RoomDetailView

app_name = 'room'

urlpatterns = [
    path('page/', RoomListView.as_view(), name='room-list'),
    path('page_deatail/', RoomDetailView.as_view(), name='room-detail')
]