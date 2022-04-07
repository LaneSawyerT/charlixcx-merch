from django.contrib import admin
from .models import Merch, Category


# Register your models here.
class MerchAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'product_name',
        'category',
        'product_price',
        'featured_image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'product_name',
    )


admin.site.register(Merch, MerchAdmin)
admin.site.register(Category, CategoryAdmin)
