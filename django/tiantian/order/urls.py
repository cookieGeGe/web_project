from django.conf.urls import url

from order import views

urlpatterns = [
    url(r'^order/', views.order, name='order'),
    url(r'^addorder/', views.addorder, name='addorder'),
    url(r'^pay_(?P<id>\d+)', views.pay, name='pay'),
]
