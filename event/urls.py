
from django.urls import path

from . import views

app_name = 'event'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_month>/', views.index, name='index'),
    path('detail/<int:event_id>/', views.detail, name='detail'),
    path('registration/', views.registration, name='registration'),
]
