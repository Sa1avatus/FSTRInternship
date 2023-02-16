from django.db import models
from django.contrib.auth.models import AbstractUser
from .statuses import STATUS_CHOICES


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(verbose_name='first name', max_length=255)
    last_name = models.CharField(verbose_name='last name', max_length=255)
    phone = models.CharField(verbose_name='phone number', max_length=20, null=True, blank=True)
    email = models.EmailField(verbose_name='e-mail', unique=True, max_length=255)


class Cords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField(default=0)


class Added(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    beauty_title = models.CharField(max_length=255, null=False)
    title = models.CharField(max_length=255, null=False)
    other_titles = models.TextField()
    connects = models.CharField(verbose_name='pass connects', max_length=255)
    cords = models.ForeignKey(Cords, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES[0])
    winter = models.CharField(verbose_name='winter difficulty level', max_length=2, null=True, blank=True)
    spring = models.CharField(verbose_name='spring difficulty level', max_length=2, null=True, blank=True)
    summer = models.CharField(verbose_name='summer difficulty level', max_length=2, null=True, blank=True)
    autumn = models.CharField(verbose_name='autumn difficulty level', max_length=2, null=True, blank=True)


class Images(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.BinaryField(null=True)
    added = models.ForeignKey(Added, related_name='added_images', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)