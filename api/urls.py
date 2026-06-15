from .views import *
from rest_framework import routers

urlpatterns = [
    
]

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('collection', CollectionViewSet, basename='collection')
router.register('accessory', AccessoryViewSet, basename='accessory')
router.register('bird', BirdViewSet, basename='bird')
router.register('cage', CageViewSet, basename='cage')
urlpatterns += router.urls