from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ImageSerializer, ProductSerializer
from .models import Image, Product
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet


class ProductViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()
  permit_list_expands = ['category', 'sites', 'comments', 'sites.company', 'sites.productsize']
  filterset_fields = ('category',)

class ImageViewSet(FlexFieldsModelViewSet):
  serializer_class = ImageSerializer
  queryset = Image.objects.all()