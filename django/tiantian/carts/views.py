from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from carts.models import CartModel


def hadcount(request, one=1):
    user = request.user
    if user != '':
        user_cart = CartModel.objects.filter(user_id=user.id, is_delete=False)
    else:
        user_cart = []
    count = len(user_cart)
    if one == 1:
        return count
    else:
        return count, user_cart


def cart(request):
    count, user_cart = hadcount(request, 2)
    data = {
        'title': '确认订单',
        'count': count,
        'msg': '请求成功',
        'code': 200,
        'cart_goods': user_cart,
    }
    return render(request, 'df_cart/cart.html', data)


def addtocart(request, gid, gnum):
    if request.user == '':
        return HttpResponseRedirect('/user/login/')
    user = request.user
    gid = int(gid)
    gnum = int(gnum)
    isexist = CartModel.objects.filter(goods_id=gid, user_id=user.id, is_delete=False).first()
    if isexist:
        cart = CartModel.objects.get(goods_id=gid, user_id=user.id)
        cart.c_num += gnum
        cart.save()
    else:
        CartModel.objects.create(
            goods_id=gid,
            user_id=user.id,
            c_num=gnum,
            is_delete=False,
        )
    if request.is_ajax():
        user_cart = CartModel.objects.filter(user_id=user.id, is_delete=False)
        count = len(user_cart)
        data = {
            'count': count,
        }
        return JsonResponse(data=data)
    else:
        return HttpResponseRedirect('/cart/')


def changcart(request, gid, gnum):
    gid = int(gid)
    gnum = int(gnum)
    cart_goods = CartModel.objects.get(id=gid)
    cart_goods.c_num = gnum
    cart_goods.save()
    data = {
        'status': 1,
        'msg': '请求成功',
    }
    return JsonResponse(data)


