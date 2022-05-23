from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

reviews_router = DefaultRouter()
reviews_router.register('products', ProductViewSet, basename='Product')