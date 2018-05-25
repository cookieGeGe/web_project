import random

import time
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import UserModel
from userauth.models import UserLogin


def login(request):
    if request.method == 'GET':
        return render(request, 'user/user_login.html')
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        users = UserModel.objects.filter(username=user, is_delete=0).exists()
        if users:
            User = UserModel.objects.get(username=user)
            if check_password(password, User.password):
                s = '1234567890qwertyuiopasdfghjklzxcvbnm'
                ticket = ''
                for i in range(15):
                    ticket += random.choice(s)
                ticket += str(int(time.time()))
                outtime = int(time.time()) + 3000
                isexists = UserLogin.objects.filter(user=User.id).exists()
                if isexists:
                    userlogin = UserLogin.objects.get(user=User)
                    userlogin.ticket = ticket
                    userlogin.out_time = outtime
                    userlogin.save()
                else:
                    UserLogin.objects.create(
                        user=User,
                        ticket=ticket,
                        out_time=outtime,
                    )
                path = request.GET.get('path')
                if path == None:
                    path = 'cart'
                response = HttpResponseRedirect('/app/%s' % path)
                # response.set_cookie('ticket', ticket, expires='过期日期')
                response.set_cookie('ticket', ticket, max_age=3000)
                return response
            else:
                return render(request, 'user/user_login.html')
        else:
            return render(request, 'user/user_login.html')


def regist(request):
    if request.method == 'GET':
        return render(request, 'user/user_register.html')

    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')
        password = make_password(password)
        UserModel.objects.create(
            username=user,
            password=password,
            email=email,
            icon=icon,
        )
        return HttpResponseRedirect('/auth/login/')


def logout(request):
    ticket = request.COOKIES.get('ticket')
    response = HttpResponseRedirect('/app/mine')
    response.delete_cookie('ticket')
    request.user = ''
    UserLogin.objects.get(ticket=ticket).delete()
    return response
