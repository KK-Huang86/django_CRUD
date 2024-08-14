from django.db import models

# Create your models here.

class Product(models.Model):
  title=models.CharField(max_length=20)
  price=models.IntegerField()
  des=models.TextField(max_length=500)
