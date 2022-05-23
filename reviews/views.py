from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ProductSerializer
from .models import Product
from rest_flex_fields.views import FlexFieldsMixin


class ProductViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()
  permit_list_expands = ['category', 'sites', 'comments', 'sites.company', 'sites.productsize']
  filterset_fields = ('category',)