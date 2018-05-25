from django.db import models


# Create your models here.

class Users(models.Model):
    u_name = models.CharField(max_length=50, unique=True)
    u_email = models.CharField(max_length=20)
    u_pass = models.CharField(max_length=255)
    u_create = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'day_users'


class UserAddr(models.Model):
    rec_peo = models.CharField(max_length=50)
    rec_addr = models.CharField(max_length=255)
    rec_tel = models.CharField(max_length=11)
    rec_code = models.IntegerField()
    user = models.ForeignKey(Users, null=True)

    class Meta:
        db_table = 'day_addr'


class UserSession(models.Model):
    out_time = models.DateTimeField()
    ticket = models.CharField(max_length=255)
    user = models.ForeignKey(Users, null=True)

    class Meta:
        db_table = 'day_usersessions'
