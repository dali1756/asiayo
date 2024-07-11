from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)