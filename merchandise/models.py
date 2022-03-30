from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    product_name = models.CharField(max_length=70)
    friendly_name = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return self.product_name

    def get_friendly_name(self):
        return self.friendly_name


class Merch(models.Model):

    class Meta:
        verbose_name_plural = 'Merch'

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    product_name = models.CharField(max_length=254)
    description = models.TextField()
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    is_limited = models.BooleanField(default=False, null=True, blank=True)
    limited_number = models.IntegerField(null=True, blank=True)
    product_hidden = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.product_name