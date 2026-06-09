from django import forms
from .models import Category, Collection, Accessory, Bird, Cage


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name', 'description']


class AccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ['name', 'description', 'price', 'size', 'color', 'photo',
                  'is_exists', 'category', 'collection']


class BirdForm(forms.ModelForm):
    class Meta:
        model = Bird
        fields = ['name', 'description', 'price', 'age', 'color', 'photo',
                  'is_exists', 'category', 'collection']


class CageForm(forms.ModelForm):
    class Meta:
        model = Cage
        fields = ['name', 'description', 'price', 'size', 'material', 'photo',
                  'is_exists', 'category', 'collection']