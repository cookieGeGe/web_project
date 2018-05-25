from django.conf.urls import url

from goods import views

urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'list(?P<id>\d+)_(?P<page>\d+)_(?P<order>\d+)/',
        views.goods_list, name='goodlist'),
    url(r'details/', views.showdetails, name='details'),
]