from django.db import models
from users.models import User

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100,unique=True)
    primaryCategory=models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Plan(models.Model):
    タイトル=models.CharField(max_length=200)
    slug=models.SlugField()
    place=models.CharField(max_length=200)
    moving_method = models.CharField(max_length=200)
    second_place = models.CharField(max_length=200)
    third_place = models.CharField(max_length=200)
    totaltime=models.IntegerField()
    created_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='photos')
    categories=models.ForeignKey('Category',on_delete=models.PROTECT)
    name=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title   