import datetime

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


from users.models import UserSession


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):

        ticket = request.COOKIES.get('ticket')
        if not ticket:
            request.user = ''
        else:
            user = UserSession.objects.filter(ticket=ticket)
            if user:
                out_time = user[0].out_time.replace(tzinfo=None)
                now_time = datetime.datetime.utcnow()
                if now_time >= out_time:
                    user[0].delete()
                    return HttpResponseRedirect('/user/login/')
                else:
                    request.user = user[0].user
