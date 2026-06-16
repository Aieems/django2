from django.contrib import admin
from .models import (
    Category, Collection, Supplier, Manufacturer,
    Accessory, Bird, Cage, Feed, Order, Pos_order
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    pass


@admin.register(Cage)
class CageAdmin(admin.ModelAdmin):
    pass


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'buyer_surname',
        'price',
        'date_create',
        'delivery_type',
    )
    list_filter = ('delivery_type', 'date_create')
    search_fields = ('buyer_firstname', 'buyer_name', 'buyer_surname', 'delivery_address')


@admin.register(Pos_order)
class PosOrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'order', 'get_product_name', 'count', 'discount')
    list_filter = ('order__date_create',)
    search_fields = ('order__buyer_firstname', 'order__buyer_name')

    @admin.display(description='Товар')
    def get_product_name(self, obj):
        product = obj.get_product()
        return product.name if product else '-'