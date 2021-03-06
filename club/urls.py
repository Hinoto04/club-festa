from django.urls import path

from . import views

app_name = 'club'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:club_id>/', views.detail, name='detail'),
    path('update/<int:club_id>/', views.update, name='update'),
    path('appli/<int:club_id>', views.appli, name='appli'),
    path('accept', views.accept, name='accept')
]
