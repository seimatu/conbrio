from django.db import models
from users.models import User

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.title

class City(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField()

    def __str__(self):
        return self.slug

    
class Plan(models.Model):
    plan_title=models.CharField(max_length=200)
    slug=models.SlugField()
    first_place = models.CharField(max_length=200)
    second_place = models.CharField(max_length=200)
    totaltime=models.IntegerField(default=10)
    created_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='photos/')
    city_name=models.ForeignKey("app.City",on_delete=models.CASCADE)
    plan_categories=models.ForeignKey('Category',on_delete=models.PROTECT)
    plan_user=models.ForeignKey("users.User",on_delete=models.CASCADE)

    def __str__(self):
        return self.plan_title

class service(models.Model):
    service_title=models.CharField(max_length=200)
    service_name=models.CharField(max_length=200)
    service_place=models.CharField(max_length=200)
    service_category=models.ForeignKey('app.Category',on_delete=models.CASCADE)

    def __str__(self):
        return self.service_title
    
    

    
