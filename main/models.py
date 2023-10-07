from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField("", max_length=50)

class Meta:
    app_label = 'main'