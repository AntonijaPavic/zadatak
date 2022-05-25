from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Posts(models.Model):
    slug=models.SlugField(unique=True,db_index=True, null=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    imageName = models.ImageField(upload_to="post",null=True)
    author=models.ForeignKey(User , on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Interijer(models.Model):
    slug=models.SlugField(unique=True,db_index=True, null=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    imageName = models.ImageField(upload_to="post",null=True)
    author=models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Eksterijer(models.Model):
    slug=models.SlugField(unique=True,db_index=True, null=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    imageName = models.ImageField(upload_to="post",null=True)
    author=models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Detail(models.Model):
    slug=models.SlugField(unique=True,db_index=True,null=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    imageName = models.ImageField(upload_to="post",null=True)
    author=models.ForeignKey(User , on_delete=models.CASCADE)
  