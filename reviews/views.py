from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ImageSerializer, MyTokenObtainPairSerializer, ProductSerializer
from .models import Image, Product
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

class ProductViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()
  permit_list_expands = ['category', 'sites', 'comments', 'sites.company', 'sites.productsize']
  filterset_fields = ('category',)


class ImageViewSet(FlexFieldsModelViewSet):
  serializer_class = ImageSerializer
  queryset = Image.objects.all()
  permission_classes = [IsAuthenticated]


class MyObtainTokenPairView(TokenObtainPairView):
  permission_classes = (AllowAny,)
  serializer_class = MyTokenObtainPairSerializer