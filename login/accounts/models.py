from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=300)

class Article(models.Model):
    categories=models.ManyToManyField(Category,blank=True)
    name=models.CharField(max_length=250)
    image = models.ImageField(upload_to="accounts", default="")
    description=models.CharField(max_length=300)