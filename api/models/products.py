
from api.models.base import BaseModel
from django.db import models

from api.models.categories import Category


class Product(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = ['name'] 
        indexes = [
            models.Index(fields=['name']),  
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return self.name