from django.urls import path

from . import views

app_name = 'event'

urlpatterns = [
    path('', views.index),
    path('registration/', views.registration, name='registration'),
]