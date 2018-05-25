from django.db import models


# Create your models here.

class ProductClass(models.Model):
    c_name = models.CharField(max_length=200)
    c_desc = models.TextField()
    c_img = models.CharField(max_length=100)

    class Meta:
        db_table = 'day_pro_class'


class Goods(models.Model):
    class_id = models.ForeignKey(ProductClass)
    pro_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pro_img = models.CharField(max_length=50)
    pro_desc = models.TextField(max_length=255)
    last_num = models.IntegerField()
    sale_num = models.IntegerField(default=0)

    class Meta:
        db_table = 'day_goods'
