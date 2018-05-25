import datetime
import random
import time

from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from carts.models import OrderModel
from carts.views import hadcount
from goods.models import Goods
from users.models import Users, UserSession, UserAddr


def login(request):
    if request.method == 'GET':
        return render(request, 'df_user/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        isexist = Users.objects.filter(u_name=username)
        if isexist:
            user = Users.objects.get(u_name=username)
            passwd = request.POST.get('pwd')
            if check_password(passwd, user.u_pass):
                s = '1234567890qwertyuiopasdfghjklzxcvbnm'
                ticket = ''
                for i in range(30):
                    ticket += random.choice(s)
                Time = time.time()
                ticket += str(int(Time))
                overtime = datetime.datetime.now() + datetime.timedelta(minutes=30)
                isexist_session = UserSession.objects.filter(user_id=user.id)
                if isexist_session:
                    for i in isexist_session:
                        i.delete()
                UserSession.objects.create(
                    ticket=ticket,
                    out_time=overtime,
                    user=user,
                )
                response = HttpResponseRedirect('/goods/index/')
                response.set_cookie('ticket', ticket, max_age=3000)
                return response

            else:
                data = {
                    'title': '登录',
                    'error_name': 0,
                    'error_pwd': 1,
                    'uname': username,
                }
                return render(request, 'df_user/login.html', data)
        else:
            data = {
                'title':'登录',
                'error_name': 1,
                'error_pwd': 0,
            }
            return render(request, 'df_user/login.html', data)


def regist(request):
    if request.method == 'GET':
        return render(request, 'df_user/register.html', {{'title':'注册'}})
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('pwd')
        email = request.POST.get('email')
        password = make_password(passwd)
        Users.objects.create(
            u_name=username,
            u_pass=password,
            u_email=email,
        )
        return HttpResponseRedirect('/user/login/', {{'title':'注册'}})


def logout(request):
    user = request.user
    UserSession.objects.get(user=user).delete()
    response = HttpResponseRedirect('/goods/index/')
    response.delete_cookie('ticket')
    return response


def site(request):
    user = request.user
    addr = UserAddr.objects.filter(user_id=user.id).first()
    if request.method == 'GET':
        data = {
            'title':'收货地址',
            'count': hadcount(request),
            'addr': addr,
        }
        return render(request, 'df_user/user_center_site.html', data)
    if request.method == 'POST':
        shou = request.POST.get('ushou')
        addrs = request.POST.get('uaddress')
        youbian = request.POST.get('uyoubian')
        phone = request.POST.get('uphone')
        if addr == None:
            UserAddr.objects.create(
                rec_addr=addrs,
                rec_peo=shou,
                rec_tel=phone,
                rec_code=youbian,
                user_id=user.id,
            )
            addr = UserAddr.objects.filter(user_id=user.id).first()
        else:
            addr.rec_peo = shou
            addr.rec_addr = addrs
            addr.rec_code = youbian
            addr.rec_tel = phone
            addr.save()
        data = {
            'title': '收货地址',
            'count': hadcount(request),
            'addr': addr,
        }
        return render(request, 'df_user/user_center_site.html', data)


def allorder(request):
    user = request.user
    page = request.GET.get('page', 1)
    allorders = OrderModel.objects.filter(user=user)
    paginator = Paginator(allorders, 2)
    pag = paginator.page(page)
    data = {
        'title': '订单中心',
        'count': hadcount(request),
        # 'allorders': allorders,
        'page': pag,
    }
    return render(request, 'df_user/user_center_order.html', data)


def userinfo(request):
    user = request.user
    users = Users.objects.get(id=user.id)

    goods = Goods.objects.filter(id__gte=1, id__lte=5)


    data = {
        'title': '个人中心',
        'count': hadcount(request),
        'user': users,
        'goods': goods,
    }
    return render(request, 'df_user/user_center_info.html', data)
