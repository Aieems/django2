from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from bird_app.models import *
from .permission import *

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [CustomSearchFilter]
    search_fields = ['name', 'description']

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [CustomSearchFilter]
    search_fields = ['name', 'description']

class AccessoryViewSet(viewsets.ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [CustomSearchFilter]
    search_fields = ['name', 'description', 'size', 'color']

class BirdViewSet(viewsets.ModelViewSet):
    queryset = Bird.objects.all()
    serializer_class = BirdSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [CustomSearchFilter]
    search_fields = ['name', 'description', 'color']

class CageViewSet(viewsets.ModelViewSet):
    queryset = Cage.objects.all()
    serializer_class = CageSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage
    filter_backends = [CustomSearchFilter]
    search_fields = ['name', 'description', 'size', 'material']