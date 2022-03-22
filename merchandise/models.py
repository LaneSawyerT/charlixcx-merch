from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=70)
    friendly_name = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name():
        return self.friendly_name


class Merch(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    product_name = models.CharField(max_length=254)
    description = models.TextField()
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    is_limited = models.BooleanField(default=False, null=True, blank=True)
    limited_number = models.IntegerField()

    def __str__(self):
        return self.name