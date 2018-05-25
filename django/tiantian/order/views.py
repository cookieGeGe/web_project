from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from carts.models import CartModel, OrderModel, OrderGoodModel
from carts.views import hadcount
from goods.models import Goods
from users.models import UserAddr


def order(request):
    user = request.user
    if request.method == 'GET':
        orderid = request.GET.getlist('orderid')
        orderlist = []
        addr = UserAddr.objects.filter(user_id=user.id)
        for i in orderid:
            cart_good = CartModel.objects.get(id=i)
            orderlist.append(cart_good)
        data = {
            'title': '添加订单',
            'count': hadcount(request),
            'orderlist': orderlist,
        }
        if addr.count() >= 1:
            data['addr'] = addr[0]
        return render(request, 'df_order/place_order.html', data)


def addorder(request):
    user = request.user
    if request.is_ajax():

        orderidlist = request.POST.getlist('id[]')
        totalpay = request.POST.get('total')
        addr = request.POST.get('address')
        status = 1
        for i in orderidlist:
            cart = CartModel.objects.get(id=i)
            if cart.c_num > Goods.objects.get(id=cart.goods.id).last_num:
                status = 2
                break
        if status == 2:
            data = {
                'msg': '请求失败',
                'status': status,
            }
            return JsonResponse(data)

        orders = OrderModel.objects.create(
            o_status=0,
            o_totalpay=totalpay,
            user_id=user.id,
            o_addr_id=addr,
            o_num=1,
        )
        good_num = 0
        for i in orderidlist:
            cart = CartModel.objects.get(id=i)
            OrderGoodModel.objects.create(
                goods_num=cart.c_num,
                goods_id=cart.goods.id,
                order_id=orders.id,
            )
            good_num += cart.c_num
            cart.delete()
        orders.o_num = good_num
        orders.save()
        data = {
            'msg': '请求成功',
            'status': status,
        }
        return JsonResponse(data)


def pay(request, id):
    order = OrderModel.objects.get(id=id)
    order.o_status = 1
    order.save()
    data = {
        'title': '付款页面',
        'id': id,
    }
    return render(request, 'df_order/pay.html', data)
