from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.postdetail, name='postdetail'),
    path('notice/<int:notice_id>/', views.noticedetail, name='noticedetail'),
    #path('testcase/', views.testcase, name='testcase')
]
