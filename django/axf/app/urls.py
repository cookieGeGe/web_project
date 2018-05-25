from django.conf.urls import url

from app import views

urlpatterns = [
    # 闪购商品查询
    url(r'^market/(?P<categoryids>\d+)/(?P<types>\d+)/(?P<orders>\d+)/', views.show, name='show'),
    # 主页
    url(r'^home/$', views.home, name='home'),
    # 闪购页面
    url(r'^market/$', views.market, name='market'),
    # 我的页面
    url(r'^mine/$', views.mine, name='mine'),
    # 没有付款
    url(r'^waitpay/$', views.orderlistwaitpay, name='orderlistwaitpay'),
    # 已经付款
    url(r'^alpay/$', views.alpay, name='orderlist'),
    # 闪购添加购物车
    url(r'^addcart/$', views.addtocart, name='addtocart'),
    # 闪购减掉商品
    url(r'^subcart/$', views.subtocart, name='subtocart'),
    # 购物车页面
    url(r'^cart/$', views.cart, name='cart'),
    # 购物车添加数量
    url(r'^addselect/$', views.addselect, name='addselect'),
    # 购物车减少数量
    url(r'^subselect/$', views.subselect, name='subselect'),
    # 改变商品状态
    url(r'^changestatus/$', views.changestatus, name='changestatus'),
    # 改变所有商品状态
    url(r'^changeall/$', views.changeall, name='changeall'),
    # 提交订单
    url(r'^order/$', views.ordergoods, name='ordergoods'),
    # 付款
    url(r'^pay/(?P<orderid>\d+)/$', views.pay, name='pay'),
    # 确认收货
    url(r'^confirm_rec/$', views.confirm_rec, name='confirm_rec'),
    # 显示我的所有订单
    url(r'^myorder/$', views.myallorder, name='myallorder'),
]
