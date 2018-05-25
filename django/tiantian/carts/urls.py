from django.conf.urls import url

from carts import views

urlpatterns =[
    url(r'^add(?P<gid>\d+)_(?P<gnum>\d+)/', views.addtocart, name='addtocart'),
    url(r'^$', views.cart, name='cart'),
    url(r'^edit(?P<gid>\d+)_(?P<gnum>\d+)', views.changcart, name='changcart'),
]