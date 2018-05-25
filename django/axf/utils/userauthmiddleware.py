import time
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from userauth.models import UserLogin


class authmiddleware(MiddlewareMixin):
    def process_request(self, request):

        ticket = request.COOKIES.get('ticket')
        if not ticket:
            pass
        else:
            user = UserLogin.objects.get(ticket=ticket)
            if user:
                if int(time.time()) >= user.out_time:
                    user.delete()
                    return HttpResponseRedirect('/auth/login/')
                else:
                    request.user = user.user
