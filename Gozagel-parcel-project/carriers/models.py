from django.db import models


# Create your models here.
class Carriers(models.Model):
    name = models.CharField(unique=True, max_length=20)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=None)
    image_url = models.CharField(max_length=50)
    ratings_amount = models.IntegerField()
