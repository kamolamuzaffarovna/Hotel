from django.urls import path
from .views import RoomListView, RoomDetailView, RoomBronView

app_name = 'room'

urlpatterns = [
    path('page/', RoomListView.as_view(), name='page-list'),
    path('page_deatail/<slug:slug>/', RoomDetailView.as_view(), name='page-detail'),
    path('room_bron/', RoomBronView.as_view(), name='room-bron')
]