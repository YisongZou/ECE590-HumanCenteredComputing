from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.urls import reverse


class Package(models.Model):
    pkgId = models.IntegerField(default=-1, primary_key=True)
    whId = models.IntegerField(default=-1)
    whX = models.IntegerField(default=-1)
    whY = models.IntegerField(default=-1)
    buyerX = models.IntegerField(default=-1)
    buyerY = models.IntegerField(default=-1)
    upsId = models.CharField(max_length=200, default='', null=True)
    truckId = models.IntegerField(default=-1)
    productStatus = models.CharField(max_length=200, default='', null=True)

    # def __str__(self):
    #  return self.pkgId


class Product(models.Model):
    productId = models.IntegerField(default=-1)
    productDescrip = models.CharField(max_length=200, default='', null=True)
    productCount = models.IntegerField(default=-1)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    # def __str__(self):
    #  return self.productId


class Truck(models.Model):
    truckId = models.IntegerField(default=-1)
    truckX = models.IntegerField(default=-1)
    truckY = models.IntegerField(default=-1)
    truckStatus = models.CharField(max_length=200, default='', null=True)
    pkgId = models.IntegerField(default=-1)

    # def __str__(self):
    #  return self.truckId

class WMUsers(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    moodRrecord = ArrayField(models.IntegerField(default= 0), blank = True, null = True)

class Doctors(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rate =  models.IntegerField(default=5)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
