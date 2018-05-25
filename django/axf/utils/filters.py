from rest_framework import filters
from app.models import Goods
import django_filters


class goodsfilter(filters.FilterSet):
    categoryid = django_filters.NumberFilter('categoryid')

    childcid = django_filters.NumberFilter('childcid')


    class Meta:
        model = Goods
        fields = ['id']
