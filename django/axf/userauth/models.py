from django.db import models

# Create your models here.
from app.models import UserModel


class UserLogin(models.Model):
    user = models.ForeignKey(UserModel)
    ticket = models.CharField(max_length=255)
    out_time = models.IntegerField(20)

    class Meta:
        db_table = 'user_cookie'
