from django import forms
from .models import Category, Collection, Accessory, Bird, Cage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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
        

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
    label='Логин пользователя',
    widget=forms.TextInput(attrs={'class':'form-control'}),
    min_length=2
    )
    email = forms.CharField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class':'form-control'}),
    )
    password1 = forms.CharField(
    label='Придумайте пароль',
    widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class':'form-control'}),
        min_length=2
    )
    password = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
