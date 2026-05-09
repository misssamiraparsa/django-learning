from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=200, db_index=True,verbose_name='عنوان')
    url_title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='active or not active')

    def __str__(self):
        return f'({self.title} - {self.url_title})'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class ProductBrand(models.Model):
    title = models.CharField(max_length=200, verbose_name='اسم برند',db_index=True)
    is_active = models.BooleanField(verbose_name='فعال یا غیرفعال')

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(
        ProductCategory,
        verbose_name='products',
        related_name='product_categories')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصوبر محصول')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True)
    price = models.IntegerField(verbose_name='price')
    short_description = models.CharField(max_length=300, null=True, verbose_name='short description')
    description = models.TextField(verbose_name='main description')
    is_active = models.BooleanField(default=False, verbose_name='active or is not active')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=100, unique=True)
    is_delete = models.BooleanField(verbose_name='is delete or not')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        #self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f"{self.title}({self.price})"


class ProductTag(models.Model):
    caption = models.CharField(max_length=100, db_index=True, verbose_name='caption')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ProductTags')

    class Meta:
        verbose_name = 'productTag'
        verbose_name_plural = 'productTags'

    def __str__(self):
        return self.caption
