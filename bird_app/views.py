from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from basket.forms import BasketAddProductForm
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
    context_object_name = 'category'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'


@method_decorator(permission_required('bird_app.add_category'), name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')


@method_decorator(permission_required('bird_app.change_category'), name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')


@method_decorator(permission_required('bird_app.delete_category'), name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


class CollectionListView(ListView):
    model = Collection
    template_name = 'collection/collection_list.html'
    context_object_name = 'collection'


class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'collection/collection_detail.html'
    context_object_name = 'collection'


@method_decorator(permission_required('bird_app.add_collection'), name='dispatch')
class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection/collection_form.html'
    success_url = reverse_lazy('collection_list')


@method_decorator(permission_required('bird_app.change_collection'), name='dispatch')
class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection/collection_form.html'
    success_url = reverse_lazy('collection_list')


@method_decorator(permission_required('bird_app.delete_collection'), name='dispatch')
class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection/collection_confirm_delete.html'
    success_url = reverse_lazy('collection_list')


class AccessoryListView(ListView):
    model = Accessory
    template_name = 'accessory/accessory_list.html'
    context_object_name = 'accessory_list'


@method_decorator(permission_required('bird_app.view_accessory'), name='dispatch')
class AccessoryDetailView(DetailView):
    model = Accessory
    template_name = 'accessory/accessory_detail.html'
    context_object_name = 'accessory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context


@method_decorator(permission_required('bird_app.add_accessory'), name='dispatch')
class AccessoryCreateView(CreateView):
    model = Accessory
    form_class = AccessoryForm
    template_name = 'accessory/accessory_form.html'
    success_url = reverse_lazy('accessory_list')


@method_decorator(permission_required('bird_app.change_accessory'), name='dispatch')
class AccessoryUpdateView(UpdateView):
    model = Accessory
    form_class = AccessoryForm
    template_name = 'accessory/accessory_form.html'
    success_url = reverse_lazy('accessory_list')


@method_decorator(permission_required('bird_app.delete_accessory'), name='dispatch')
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context


@method_decorator(permission_required('bird_app.add_bird'), name='dispatch')
class BirdCreateView(CreateView):
    model = Bird
    form_class = BirdForm
    template_name = 'bird/bird_form.html'
    success_url = reverse_lazy('bird_list')


@method_decorator(permission_required('bird_app.change_bird'), name='dispatch')
class BirdUpdateView(UpdateView):
    model = Bird
    form_class = BirdForm
    template_name = 'bird/bird_form.html'
    success_url = reverse_lazy('bird_list')


@method_decorator(permission_required('bird_app.delete_bird'), name='dispatch')
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context


@method_decorator(permission_required('bird_app.add_cage'), name='dispatch')
class CageCreateView(CreateView):
    model = Cage
    form_class = CageForm
    template_name = 'cage/cage_form.html'
    success_url = reverse_lazy('cage_list')


@method_decorator(permission_required('bird_app.change_cage'), name='dispatch')
class CageUpdateView(UpdateView):
    model = Cage
    form_class = CageForm
    template_name = 'cage/cage_form.html'
    success_url = reverse_lazy('cage_list')


@method_decorator(permission_required('bird_app.delete_cage'), name='dispatch')
class CageDeleteView(DeleteView):
    model = Cage
    template_name = 'cage/cage_confirm_delete.html'
    success_url = reverse_lazy('cage_list')


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'auth/login.html', context)


def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('home')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'auth/registration.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


class ProductsView(TemplateView):
    template_name = 'products/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accessory_list'] = Accessory.objects.all()
        context['bird_list'] = Bird.objects.all()
        context['cage_list'] = Cage.objects.all()
        context['feed_list'] = Feed.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class OrdersView(TemplateView):
    template_name = 'orders/orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_list'] = Order.objects.filter(
            user=self.request.user
        ).order_by('-date_create')
        return context