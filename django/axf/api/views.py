from django.shortcuts import render

from utils.filters import goodsfilter
from rest_framework import mixins, viewsets

# Create your views here.
from app.models import Goods, Foodtype
from utils.serializers import goodsserializers


class getgoods(mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               viewsets.GenericViewSet):
    queryset = Goods.objects.all()

    filter_class = goodsfilter

    serializer_class = goodsserializers

    def get_queryset(self):
        orders = self.request.GET.get('orderid')
        data = self.queryset
        if orders:
            orders = int(orders)
            if orders == 0:
                data = data.order_by('id')
            elif orders == 1:
                data = data.order_by('productnum')
            elif orders == 2:
                data = data.order_by('-price')
            else:
                data = data.order_by('price')
        return data

