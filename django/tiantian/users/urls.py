from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^regist/', views.regist, name='regist'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^site/', views.site, name='site'),
    url(r'^userorder/', views.allorder, name='userorder'),
    url(r'^info/', views.userinfo, name='userinfo'),
]
