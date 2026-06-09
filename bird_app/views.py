from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy
from .forms import *

# Create your views here.

def home_views(request):
    return render(request, 'home.html')

def about_views(request):
    return render(request, 'about/about.html')

def contacts_views(request):
    return render(request, 'about/contacts.html')

def location_views(request):
    return render(request, 'about/location.html')

def products_views(request):
    return render(request, 'products/products.html')

def categories_views(request):
    return render(request, 'products/categories.html')

def all_products_views(request):
    return render(request, 'products/all_products.html')

def cart_views(request):
    return render(request, 'cart.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'category_list'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

class CollectionListView(ListView):
    model = Collection
    template_name = 'collection/collection_list.html'
    context_object_name = 'collection_list'

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'collection/collection_detail.html'
    context_object_name = 'collection'

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection/collection_form.html'
    success_url = reverse_lazy('collection_list')

class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection/collection_form.html'
    success_url = reverse_lazy('collection_list')

class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection/collection_confirm_delete.html'
    success_url = reverse_lazy('collection_list')

class AccessoryListView(ListView):
    model = Accessory
    template_name = 'accessory/accessory_list.html'
    context_object_name = 'accessory_list'

class AccessoryDetailView(DetailView):
    model = Accessory
    template_name = 'accessory/accessory_detail.html'
    context_object_name = 'accessory'

class AccessoryCreateView(CreateView):
    model = Accessory
    form_class = AccessoryForm
    template_name = 'accessory/accessory_form.html'
    success_url = reverse_lazy('accessory_list')

class AccessoryUpdateView(UpdateView):
    model = Accessory
    form_class = AccessoryForm
    template_name = 'accessory/accessory_form.html'
    success_url = reverse_lazy('accessory_list')

class AccessoryDeleteView(DeleteView):
    model = Accessory
    template_name = 'accessory/accessory_confirm_delete.html'
    success_url = reverse_lazy('accessory_list')

class BirdListView(ListView):
    model = Bird
    template_name = 'bird/bird_list.html'
    context_object_name = 'bird_list'

class BirdDetailView(DetailView):
    model = Bird
    template_name = 'bird/bird_detail.html'
    context_object_name = 'bird'

class BirdCreateView(CreateView):
    model = Bird
    form_class = BirdForm
    template_name = 'bird/bird_form.html'
    success_url = reverse_lazy('bird_list')

class BirdUpdateView(UpdateView):
    model = Bird
    form_class = BirdForm
    template_name = 'bird/bird_form.html'
    success_url = reverse_lazy('bird_list')

class BirdDeleteView(DeleteView):
    model = Bird
    template_name = 'bird/bird_confirm_delete.html'
    success_url = reverse_lazy('bird_list')

class CageListView(ListView):
    model = Cage
    template_name = 'cage/cage_list.html'
    context_object_name = 'cage_list'

class CageDetailView(DetailView):
    model = Cage
    template_name = 'cage/cage_detail.html'
    context_object_name = 'cage'

class CageCreateView(CreateView):
    model = Cage
    form_class = CageForm
    template_name = 'cage/cage_form.html'
    success_url = reverse_lazy('cage_list')

class CageUpdateView(UpdateView):
    model = Cage
    form_class = CageForm
    template_name = 'cage/cage_form.html'
    success_url = reverse_lazy('cage_list')

class CageDeleteView(DeleteView):
    model = Cage
    template_name = 'cage/cage_confirm_delete.html'
    success_url = reverse_lazy('cage_list')