from django.urls import path
from .views import *

urlpatterns = [
    path('', home_views, name='home'),
    path('about/', about_views, name='about'),
    path('about/contacts/', contacts_views, name='contacts'),
    path('about/location/', location_views, name='location'),
    path('products/', ProductsView.as_view(), name='products'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('products/categories/', CategoryListView.as_view(template_name='products/categories.html'), name='categories'),    path('products/all/', AccessoryListView.as_view(template_name='products/all_products.html'), name='all_products'),
    path('cart/', cart_views, name='cart'),

    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('collection/', CollectionListView.as_view(), name='collection_list'),
    path('collection/<int:pk>/', CollectionDetailView.as_view(), name='collection_detail'),
    path('collection/create/', CollectionCreateView.as_view(), name='collection_create'),
    path('collection/<int:pk>/update/', CollectionUpdateView.as_view(), name='collection_update'),
    path('collection/<int:pk>/delete/', CollectionDeleteView.as_view(), name='collection_delete'),

    path('accessory/', AccessoryListView.as_view(), name='accessory_list'),
    path('accessory/<int:pk>/', AccessoryDetailView.as_view(), name='accessory_detail'),
    path('accessory/create/', AccessoryCreateView.as_view(), name='accessory_create'),
    path('accessory/<int:pk>/update/', AccessoryUpdateView.as_view(), name='accessory_update'),
    path('accessory/<int:pk>/delete/', AccessoryDeleteView.as_view(), name='accessory_delete'),

    path('bird/', BirdListView.as_view(), name='bird_list'),
    path('bird/<int:pk>/', BirdDetailView.as_view(), name='bird_detail'),
    path('bird/create/', BirdCreateView.as_view(), name='bird_create'),
    path('bird/<int:pk>/update/', BirdUpdateView.as_view(), name='bird_update'),
    path('bird/<int:pk>/delete/', BirdDeleteView.as_view(), name='bird_delete'),

    path('cage/', CageListView.as_view(), name='cage_list'),
    path('cage/<int:pk>/', CageDetailView.as_view(), name='cage_detail'),
    path('cage/create/', CageCreateView.as_view(), name='cage_create'),
    path('cage/<int:pk>/update/', CageUpdateView.as_view(), name='cage_update'),
    path('cage/<int:pk>/delete/', CageDeleteView.as_view(), name='cage_delete'),


    path('login/', login_user, name='login_page'),
    path('registration/', registration_user, name='registration_page'),
    path('logout/', logout_user, name='logout_page'),


]