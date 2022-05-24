from django.contrib import admin
from django.contrib.auth.models import Group

from reviews.models import Category, Company, Product, ProductSite, ProductSize, Comment, Image

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProductSize)
admin.site.register(ProductSite)
admin.site.register(Comment)
admin.site.register(Image)

admin.site.unregister(Group)

admin.site.site_header = "Product Review Admin"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'content')