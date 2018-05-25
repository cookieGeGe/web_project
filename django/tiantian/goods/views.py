from django.shortcuts import render
from django.core.paginator import Paginator
from goods.models import Goods, ProductClass
from carts.views import hadcount


# Create your views here.

def index(request):
    goods = Goods.objects.all()
    data = {
        'count': hadcount(request),
        'title': '天天生鲜首页',
        'fruits': goods.filter(class_id_id=1)[:4],
        'hais': goods.filter(class_id_id=2)[:4],
        'rous': goods.filter(class_id_id=3)[:4],
        'qins': goods.filter(class_id_id=4)[:4],
        'cais': goods.filter(class_id_id=5)[:4],
        'dongs': goods.filter(class_id_id=6)[:4],
    }

    return render(request, 'df_goods/index.html', data)


def goods_list(request, id, page, order):
    if int(order) == 1:
        orders = 'id'
    elif int(order) == 2:
        orders = 'price'
    else:
        orders = 'sale_num'
    goods = Goods.objects.filter(class_id_id=id).order_by(orders)
    page_ob = Paginator(goods, 5)
    show_page = page_ob.page(page)
    newgood = goods[:2]
    title = ProductClass.objects.get(id=id)
    data = {
        'title': title.c_name,
        'count': hadcount(request),
        'proid': id,
        'showpage': show_page,
        'page': page,
        'order': order,
        'newgood': newgood,
    }

    return render(request, 'df_goods/list.html', data)


def showdetails(request):
    proid = request.GET.get('good')
    good = Goods.objects.get(id=proid)
    newgood = Goods.objects.all()[:2]
    data = {
        'title': '商品详情',
        'count': hadcount(request),
        'good': good,
        'newgood': newgood,
    }

    return render(request, 'df_goods/detail.html', data)
