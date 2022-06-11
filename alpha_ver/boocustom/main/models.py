import os
from django.db import models
from django.conf import settings
from .choice import *

class Country(models.Model):
    nickname = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='닉네임')
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=10, verbose_name="나라", blank=True, null=True)

    def __str__(self):
        return str(self.nickname)

    class Meta:
        db_table = 'Country'
        verbose_name = 'Country'
        verbose_name_plural = 'Country'

class Image(models.Model):
    nickname = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='닉네임')
    image = models.ImageField(upload_to='images/',verbose_name='이미지', blank=True, null=True)

    def __str__(self):
        return str(self.nickname)

    class Meta:
        db_table = 'Image'
        verbose_name = 'Image'
        verbose_name_plural = 'Image'

class Greetings(models.Model):
    nickname = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='닉네임')
    greetings = models.CharField(max_length=40, verbose_name='인삿말', blank=True, null=True)


    def __str__(self):
        return str(self.nickname)

    class Meta:
        db_table = 'Greetings'
        verbose_name = 'Greetings'
        verbose_name_plural = 'Greetings'