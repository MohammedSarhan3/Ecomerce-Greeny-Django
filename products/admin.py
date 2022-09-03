from django.contrib import admin
from .models import Product , ProdectReview , ProudectImages ,Category ,Brand
# Register your models here.

class ProductImagesInline(admin.TabularInline):
    model =ProudectImages

class ProductAdmin(admin.ModelAdmin):
    listdisplay=['name','price','flag']
    inlines = [ProductImagesInline]


admin.site.register(Product,ProductAdmin)
admin.site.register(ProdectReview)
admin.site.register(ProudectImages)
admin.site.register(Category)
admin.site.register(Brand)