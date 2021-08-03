from django.urls import path

from . import views

app_name = 'club'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:club_id>/', views.detail, name='detail'),
]
