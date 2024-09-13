from django.contrib import admin

from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    """Админка Джанго с настройками."""

    empty_value_display = 'Не задано'
    list_display = (
        'name',
        'price'
    )
    search_fields = ('name',)
    list_filter = (
        'price',
    )
    list_display_links = ('name',)


admin.site.register(Product, ProductAdmin)
