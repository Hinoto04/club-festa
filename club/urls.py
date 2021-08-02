from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:club_id>/', views.detail),
]
