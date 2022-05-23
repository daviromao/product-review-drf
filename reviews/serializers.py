from .models import (
  Category,
  Company,
  Product, 
  ProductSite, 
  ProductSize,
  Comment,
)

from django.contrib.auth.models import User

from rest_flex_fields import FlexFieldsModelSerializer

class CompanySerializer(FlexFieldsModelSerializer):
  class Meta:
    model = Company
    fields = ['id', 'name', 'url']


class CategorySerializer(FlexFieldsModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'name']


class ProductSizeSerializer(FlexFieldsModelSerializer):
  class Meta:
    model = ProductSize
    fields = ['id', 'name']


class ProductSiteSerializer(FlexFieldsModelSerializer):
  class Meta:
    model = ProductSite
    fields = ['id', 'name', 'price', 'url', 'created', 'updated']
    expandable_fields = {
      'product': 'reviews.CategorySerializer',
      'productsize': 'reviews.ProductSizeSerializer',
      'company': 'reviews.CompanySerializer',
    }


class ProductSerializer(FlexFieldsModelSerializer):  
  class Meta:
    model = Product
    fields = ['id', 'name', 'content', 'created', 'updated']
    expandable_fields = {
      'category': ('reviews.CategorySerializer', {'many': True}),
      'sites': ('reviews.ProductSiteSerializer', {'many': True}),
      'comments': ('reviews.CommentSerializer', {'many': True}),
    }


class UserSerializer(FlexFieldsModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username']
  
class CommentSerializer(FlexFieldsModelSerializer):
  class Meta:
    model = Comment
    fields = ['pk', 'title', 'content', 'created', 'updated']
    expandable_fields = {
        'product': 'reviews.CategorySerializer',
        'user': 'reviews.UserSerializer',
    }