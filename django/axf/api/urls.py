from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from api import views
from api.views import getgoods

router = SimpleRouter()

router.register(r'goods', views.getgoods)

urlpatterns = []

urlpatterns += router.urls
