from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from app.models import MainWheel, MainNav, MainShop, \
    MainShow, Mainmustbuy, Foodtype, OrderModel, Goods, \
    CartModel, OrderGoodModel


# Create your views here.

def home(request):
    wheel = MainWheel.objects.all()
    nav = MainNav.objects.all()
    mustbuy = Mainmustbuy.objects.all()
    shop = MainShop.objects.all()
    mainshow = MainShow.objects.all()
    data = {
        'wheels': wheel,
        'navs': nav,
        'mustbuys': mustbuy,
        'shop1': shop[0],
        'shop2': shop[1:3],
        'shop3': shop[3:7],
        'shop4': shop[7:],
        'shows': mainshow,
    }
    return render(request, 'home/home.html', data)


def market(request):
    return HttpResponseRedirect(
        reverse('axf:show',
                kwargs={'categoryids': 104749, 'types': 0, 'orders': 0}),
    )


def show(request, categoryids=104749, types=0, orders=0):
    if int(types) == 0:
        data = Goods.objects.filter(categoryid=categoryids)
    else:
        data = Goods.objects.filter(categoryid=categoryids, childcid=types)
    orders = int(orders)
    if orders == 0:
        data = data.order_by('id')
    elif orders == 1:
        data = data.order_by('productnum')
    elif orders == 2:
        data = data.order_by('-price')
    else:
        data = data.order_by('price')
    foottypes = Foodtype.objects.all()

    footchilds = Foodtype.objects.get(typeid=categoryids).childtypenames.split('#')

    footchildlist = []
    for footchild in footchilds:
        footchildlist.append(footchild.split(':'))
    datas = {
        'foottypes': foottypes,
        'data': data,
        'types': footchildlist,
        'cateid': categoryids,
        'typeid': types,
        'orderid': orders,
    }
    return render(request, 'market/market.html', datas)


def cart(request):
    if request.user.id != None:
        user = request.user
        carts = CartModel.objects.filter(user=user)
        isall = True
        for i in range(len(carts) - 1):
            if carts[i].is_delete != carts[i + 1].is_delete:
                isall = False
                break
        return render(request, 'cart/cart.html', {'carts': carts, 'isall': isall})
    else:
        return HttpResponseRedirect('/auth/login/')


def mine(request):
    un_pay = 0
    al_pay = 0
    if request.user.id:
        user = request.user
        for ordermodel in OrderModel.objects.filter(user=user.id, o_status__lt=3):
            if ordermodel.o_status == 0:
                un_pay += 1
            else:
                al_pay += 1
    data = {
        'un_pay': un_pay,
        'al_pay': al_pay,
    }
    return render(request, 'mine/mine.html', data)


def alpay(request):
    user = request.user

    datas = OrderModel.objects.filter(user=user.id, o_status__lt=3, o_status__gt=0)
    return render(request, 'order/order_list_payed.html', {'datas': datas})


def orderlistwaitpay(request):
    user = request.user
    data = OrderModel.objects.filter(user=user.id, o_status=0)
    return render(request, 'order/order_list_wait_pay.html', {'datas': data})


def addtocart(request):
    if request.method == 'POST':
        goodid = request.POST.get('goodsid')
        user = request.user

        if user.id == None:
            return HttpResponseRedirect('/auth/login/?path=market')

        data = {
            'code': 200,
            'msg': '请求成功'
        }

        if CartModel.objects.filter(goods_id=goodid).exists():
            cart = CartModel.objects.get(goods_id=goodid)
            cart.c_num += 1
            cart.save()
        else:
            CartModel.objects.create(
                c_num=1,
                user=user,
                goods_id=goodid,
                is_delete=False,
            )
        data['c_num'] = CartModel.objects.get(goods_id=goodid).c_num
        return JsonResponse(data)


def subtocart(request):
    if request.method == 'POST':
        goodid = request.POST.get('goodid')
        user = request.user

        if user.id == None:
            return HttpResponseRedirect('/auth/login/?path=market')

        data = {
            'code': 200,
            'msg': '请求成功'
        }

        if CartModel.objects.filter(goods_id=goodid, is_delete=False).exists():
            user = CartModel.objects.get(goods_id=goodid, is_delete=False)
            if user.c_num > 1:
                user.c_num -= 1
                user.save()
                data['c_num'] = user.c_num
                return JsonResponse(data)
            else:
                user.delete()
        data['c_num'] = 0
        return JsonResponse(data)


def subselect(request):
    if request.method == 'POST':
        cartid = request.POST.get('cartid')
        carts = CartModel.objects.get(id=cartid)
        data = {
            'msg': '请求成功',
            'code': 200,
        }
        if carts.c_num > 1:
            carts.c_num -= 1
            carts.save()
            data['c_num'] = carts.c_num
            return JsonResponse(data)
        else:
            carts.is_delete = True
            carts.c_num = 0
            carts.save()
            data['c_num'] = 0
            return JsonResponse(data)


def addselect(request):
    if request.method == 'POST':
        cartid = request.POST.get('cartid')
        carts = CartModel.objects.get(id=cartid)

        data = {
            'msg': '请求成功',
            'code': 200,
        }

        if carts.c_num == 0:
            carts.is_delete = False
            carts.c_num = 1
            carts.save()
            data['c_num'] = 1
            return JsonResponse(data)
        else:
            carts.c_num += 1
            carts.save()
            data['c_num'] = carts.c_num
            return JsonResponse(data)


def changestatus(request):
    if request.method == 'POST':
        cartid = request.POST.get('cartid')
        carts = CartModel.objects.get(id=cartid)
        data = {
            'msg': '请求成功',
            'code': 200,
        }
        if carts.is_delete:
            carts.is_delete = False
            carts.save()
        else:
            carts.is_delete = True
            carts.save()
        data['is_delete'] = carts.is_delete
        return JsonResponse(data)


def changeall(request):
    if request.method == 'POST':
        istrue = request.POST.get('istrue')
        user = request.user

        carts = CartModel.objects.filter(user=user)
        data = {
            'msg': '请求成功',
            'code': 200,
        }

        for cart in carts:
            if cart.is_delete != int(istrue):
                cart.is_delete = int(istrue)
                cart.save()
        return JsonResponse(data)


def ordergoods(request):
    user = request.user
    carts = CartModel.objects.filter(user=user, is_delete=False)
    order1 = OrderModel.objects.create(
        user=user,
        o_num=1,
    )
    orderid = order1.id
    o_num = 0
    for cart in carts:
        OrderGoodModel.objects.create(
            goods=cart.goods,
            order=order1,
            goods_num=cart.c_num
        )
        o_num += cart.c_num
    order1.o_num = o_num
    order1.save()
    CartModel.objects.filter(user=user).delete()
    return HttpResponseRedirect(
        reverse('axf:pay', args=(str(orderid),))
    )


def pay(request, orderid):
    if request.method == 'GET':
        user = request.user
        orderpay = orderid
        goodspay = OrderGoodModel.objects.filter(order_id=orderpay)
        data = {
            'user': user,
            'orderpay': orderpay,
            'goodspay': goodspay,
        }
        return render(request, 'order/order_info.html', data)
    if request.method == 'POST':
        orderid = request.POST.get('orderid')
        orderpay1 = OrderModel.objects.get(id=orderid)
        orderpay1.o_status = 1
        orderpay1.save()
        data = {
            'urls': '/app/mine/',
        }
        return JsonResponse(data)


def confirm_rec(request):
    if request.method == 'POST':
        orderid = request.POST.get('orderid')

        orders = OrderModel.objects.get(id=orderid)

        orders.o_status = 3
        orders.save()

        data = {
            'msg': '请求成功',
            'code': 200,
        }

        return JsonResponse(data)


def myallorder(request):
    user = request.user

    datas = OrderModel.objects.filter(user=user.id)
    return render(request, 'order/myorder.html', {'datas': datas})
