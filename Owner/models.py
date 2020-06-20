from django.db import models
from django.contrib.auth.models import User


class owner(models.Model):
    name = models.CharField('名前', max_length=100)
    age = models.IntegerField('年齢', max_length=2)
    email = models.EmailField('Eメール', unique=True)
    phone_number = models.DecimalField('電話番号', max_digits=12, decimal_places=0)
    photo = models.ImageField(upload_to='/images', default=True, blank=True, null=True)
    user_id = models.ForeignKey(User, verbose_name='Authuser', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class dogs(models.Model):
    name = models.CharField('名前', max_length=100)
    age = models.IntegerField('年齢', max_length=2)
    photo = models.ImageField(upload_to='/images', default=True, blank=True, null=True)
    user_id = models.ForeignKey(User, verbose_name='Authuser', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class cats(models.Model):
    name = models.CharField('名前', max_length=100)
    age = models.IntegerField('年齢', max_length=2)
    photo = models.ImageField(upload_to='/images', default=True, blank=True, null=True)
    user_id = models.ForeignKey(User, verbose_name='Authuser', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
