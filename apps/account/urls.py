from django.urls import path, reverse_lazy
from .views import LoginView, LogoutView, RegisterView
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html',
                                                next_page=reverse_lazy('main:home')), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register')
]