from django.db import models
from django.contrib.auth.models import AbstractUser
from .statuses import STATUS_CHOICES


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(verbose_name='first name', max_length=255)
    last_name = models.CharField(verbose_name='last name', max_length=255)
    patronymic_name = models.CharField(verbose_name='last name', max_length=255)
    phone = models.CharField(verbose_name='phone number', max_length=20, null=True, blank=True)
    email = models.EmailField(verbose_name='e-mail', unique=True, max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = self.email
        super(User, self).save(*args, **kwargs)


class Cords(models.Model):
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    height = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.latitude}, {self.longitude}: {self.height} meters'


class Added(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    beauty_title = models.CharField(max_length=255, null=False)
    title = models.CharField(max_length=255, null=False)
    other_titles = models.TextField()
    connects = models.CharField(verbose_name='pass connects', null=True, max_length=255)
    cords = models.ForeignKey(Cords, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=STATUS_CHOICES[0])
    winter = models.CharField(verbose_name='winter difficulty level', max_length=2, null=True, blank=True)
    spring = models.CharField(verbose_name='spring difficulty level', max_length=2, null=True, blank=True)
    summer = models.CharField(verbose_name='summer difficulty level', max_length=2, null=True, blank=True)
    autumn = models.CharField(verbose_name='autumn difficulty level', max_length=2, null=True, blank=True)

    def __str__(self):
        return f'{self.title}, {self.cords}: {self.status}'

    def set_levels(self, **kwargs):
        self.winter = kwargs.get('winter', '')
        self.spring = kwargs.get('spring', '')
        self.summer = kwargs.get('summer', '')
        self.autumn = kwargs.get('autumn', '')
        self.save()

    def get_levels(self):
        dict_levels = {}
        dict_levels['winter'] = self.winter
        dict_levels['spring'] = self.spring
        dict_levels['summer'] = self.summer
        dict_levels['autumn'] = self.autumn
        return dict_levels


class Images(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.BinaryField(null=True)
    added = models.ForeignKey(Added, related_name='added_images', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)