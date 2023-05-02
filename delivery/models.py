from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product_name} - {self.quantity}"
