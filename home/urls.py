from django.contrib.auth.forms import PasswordChangeForm
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('checkid/', views.checkmail, name='checkmail'),
    path('login/', auth_views.LoginView.as_view(template_name='home/home_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/', views.user, name='user'),
    path('user/<int:userid>', views.user, name='user'),
    path('edit/', views.edit, name='edit'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
    #path('usercreate/', views.accountcreate, name='usercreate'),
]
