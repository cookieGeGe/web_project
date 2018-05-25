from django.db import models
from users.models import Users, UserAddr
from goods.models import Goods


# Create your models here.

class CartModel(models.Model):
    user = models.ForeignKey(Users)  # 关联用户
    goods = models.ForeignKey(Goods)  # 关联商品
    c_num = models.IntegerField(default=1)  # 商品数量
    is_delete = models.BooleanField(default=True)

    class Meta:
        db_table = 'day_cart'


class OrderModel(models.Model):
    user = models.ForeignKey(Users)
    o_num = models.CharField(max_length=64)
    # 状态 0表示已下单，未付款， 1，代表已付款没有发货， 2，代表已付款已发货,3表示已收货
    o_status = models.IntegerField(default=0)
    o_create = models.DateTimeField(auto_now=True)
    o_totalpay = models.CharField(max_length=255,null=True)
    o_addr = models.ForeignKey(UserAddr, null=True)

    class Meta:
        db_table = 'day_order'


class OrderGoodModel(models.Model):
    goods = models.ForeignKey(Goods)
    order = models.ForeignKey(OrderModel)
    goods_num = models.IntegerField(default=1)

    class Meta:
        db_table = 'day_order_goods'
