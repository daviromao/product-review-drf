from rest_framework.routers import DefaultRouter
from .views import ImageViewSet, ProductViewSet

reviews_router = DefaultRouter()
reviews_router.register('products', ProductViewSet, basename='Product')
reviews_router.register('images', ImageViewSet, basename='Image')
