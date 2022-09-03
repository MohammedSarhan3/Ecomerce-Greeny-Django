from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.contrib.auth.models import User     
from taggit.managers import TaggableManager             


PRODUCT_FLAG = (
    ('New','New'),
    ('Feature','Feature'),
    ('Sale','Sale'),
)
class Product(models.Model):
    name =models.CharField(_('Nmae'),max_length=100)#First parameter her is verbose_name
    sku =models.IntegerField(_('SKU'))#First parameter her is verbose_name
    subtitles=models.CharField(_('Subtitles'),max_length=300)#First parameter her is verbose_name
    desc = models.TextField(_('Descreption'),max_length=10000)#First parameter her is verbose_name
    flag =models.CharField(_('Flag'),max_length=10 ,choices=PRODUCT_FLAG)
    price = models.FloatField(_('Price'))
    tags=TaggableManager()
    category = models.ForeignKey('Category',verbose_name=_('Category'), related_name='product_category',on_delete=models.SET_NULL,null=True,blank=True)
    Brand = models.ForeignKey('Brand',verbose_name=_('Brand'), related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    video = models.URLField(_('Video'),null=True , blank=True)

    def __str__(self):
        return self.name

class ProudectImages(models.Model):
    Product= models.ForeignKey(Product,verbose_name=_('Product_image'), related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(_('Image'),upload_to='product images')

    def __str__(self):
        return str(self.product)


class Category(models.Model):
    name = models.CharField(max_length=100 , verbose_name=_('Name'))
    image = models.ImageField(_('Image'),upload_to='category') #First parameter her is verbose_name

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(_('Name'),max_length=100)#First parameter her is verbose_name
    image = models.ImageField(_('Image'),upload_to='barnd')#First parameter her is verbose_name
    def __str__(self):
            return self.name
class ProdectReview(models.Model):
    user= models.ForeignKey(User, related_name='user_review',on_delete= models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,verbose_name=_('Product'),related_name='product_review', on_delete=models.SET_NULL,null=True,blank=True)
    rate =models.IntegerField(_('Rate'))
    review =models.CharField(_('review'),max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.product)