from app.models import Goods, Foodtype
from rest_framework import serializers


class goodsserializers(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['productid', 'productimg', 'price', 'marketprice', 'categoryid', 'productnum']
