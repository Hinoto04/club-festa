from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('checkid', views.checkmail, name='checkmail'),
    path('login', auth_views.LoginView.as_view(template_name='home/home_login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('user', views.user, name='user')
]
