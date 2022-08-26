from distutils.command.upload import upload
from tabnanny import verbose
from turtle import title
from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000,null=True,blank=True)
    publish_date = models.DateField(default= timezone.now)
    uodate_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'posts/' ,null=True , blank = True)
    category = models.ForeignKey(Category ,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'My Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']


    def __str__(self):
        return self.title