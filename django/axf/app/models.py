from django.db import models


# Create your models here.

class Main(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=16)

    # 将该类抽象
    class Meta:
        abstract = True


class MainWheel(Main):
    # 图片轮播
    class Meta:
        db_table = 'axf_wheel'


class MainNav(Main):
    # 导航
    class Meta:
        db_table = 'axf_nav'


class MainShop(Main):
    # 导航
    class Meta:
        db_table = 'axf_shop'


class Mainmustbuy(Main):
    class Meta:
        db_table = 'axf_mustbuy'


class MainShow(Main):
    categoryid = models.CharField(max_length=16)
    brandname = models.CharField(max_length=100)
    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=16)
    productid1 = models.CharField(max_length=16)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField(default=0)
    marketprice1 = models.FloatField(default=1)
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=16)
    productid2 = models.CharField(max_length=16)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=5, default=0)
    marketprice2 = models.FloatField(default=1)
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=16)
    productid3 = models.CharField(max_length=16)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=5, default=0)
    marketprice3 = models.FloatField(default=1)

    class Meta:
        db_table = 'axf_mainshow'


# 闪购
class Foodtype(models.Model):
    typeid = models.CharField(max_length=16)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_foodtypes'


class Goods(models.Model):
    productid = models.CharField(max_length=16)  # 商品id
    productimg = models.CharField(max_length=200)  # 商品图片
    productname = models.CharField(max_length=100)  # 商品名称
    productlongname = models.CharField(max_length=200)  # 商品规格
    isxf = models.IntegerField(default=1)
    pmdesc = models.CharField(max_length=100)
    specifics = models.CharField(max_length=100)  # 详细规格
    price = models.FloatField(default=0)  # 折后价格
    marketprice = models.FloatField(default=1)  # 原价
    categoryid = models.CharField(max_length=16)  # 分类id
    childcid = models.CharField(max_length=16)  # 子分类id
    childcidname = models.CharField(max_length=100)  # 子分类id名称
    dealerid = models.CharField(max_length=16)
    storenums = models.IntegerField(default=1)  # 排序要使用到的id
    productnum = models.IntegerField(default=1)  # 销量

    class Meta:
        db_table = 'axf_goods'


class UserModel(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=64, unique=True)
    sex = models.BooleanField(default=False)
    icon = models.ImageField(upload_to='icons')  # 头像
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'axf_users'


class CartModel(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    goods = models.ForeignKey(Goods)  # 关联商品
    c_num = models.IntegerField(default=1)  # 商品数量
    is_delete = models.BooleanField(default=True)

    class Meta:
        db_table = 'axf_cart'


class OrderModel(models.Model):
    user = models.ForeignKey(UserModel)
    o_num = models.CharField(max_length=64)
    # 状态 0表示已下单，未付款， 1，代表已付款没有发货， 2，代表已付款已发货,3表示已收货
    o_status = models.IntegerField(default=0)
    o_create = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'axf_order'


class OrderGoodModel(models.Model):
    goods = models.ForeignKey(Goods)
    order = models.ForeignKey(OrderModel)
    goods_num = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_order_goods'
