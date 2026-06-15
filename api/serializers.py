from rest_framework import serializers
from bird_app.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            'name',
            'description',
        ]
class AccessorySerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    class Meta:
        model = Accessory
        fields = [
            'name',
            'description',
            'price',
            'size',
            'color',
            'photo',
            'is_exists',
            'category',
            'collection',
        ]
class BirdSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    class Meta:
        model = Bird
        fields = [
            'name',
            'description',
            'price',
            'age',
            'color',
            'photo',
            'is_exists',
            'category',
            'collection',
        ]
class CageSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    class Meta:
        model = Cage
        fields = [
            'name',
            'description',
            'price',
            'size',
            'material',
            'photo',
            'is_exists',
            'category',
            'collection',
        ]