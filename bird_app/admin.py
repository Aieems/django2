from django.contrib import admin
from .models import (
    Category, Collection, Supplier, Manufacturer,
    Accessory, Bird, Cage, Feed
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
