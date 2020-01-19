from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='photos',default=1)
    primaryCategory=models.BooleanField(default=False)
    slug=models.SlugField()

    def __str__(self):
        return self.slug

class Plan(models.Model):
    title=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    moving_method = models.CharField(max_length=200)
    second_place = models.CharField(max_length=200)
    third_place = models.CharField(max_length=200)
    totaltime=models.IntegerField()
    created_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='photos')
    categories=models.ForeignKey('Category',on_delete=models.PROTECT)

    def __str__(self):
        return self.title