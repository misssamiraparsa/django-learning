from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class ProductTag(models.Model):
    tag = models.CharField(max_length=100, verbose_name='tag title')

    class Meta:
        verbose_name = 'productTag'
        verbose_name_plural = 'productTags'

    def __str__(self):
      return self.tag


class ProductCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, verbose_name='عنوان در url')

    def __str__(self):
        return f'({self.title} - {self.url_title})'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class ProductInformation(models.Model):
    color = models.CharField(max_length=100, verbose_name='color')
    size = models.CharField(max_length=100, verbose_name='size')

    class Meta:
        verbose_name = 'productInformation'
        verbose_name_plural = 'productInformations'

    def __str__(self):
        return f'({self.color} - {self.size})'


class Product(models.Model):
    title = models.CharField(max_length=100)

    product_tags = models.ManyToManyField(
        ProductTag,
        null=True,
        blank=True,
        verbose_name='product tags',
        related_name='product_tags'
    )
    product_information = models.OneToOneField(
        ProductInformation,
        on_delete=models.CASCADE,
        related_name='product_information',
        verbose_name='اطلاعات تکمیلی',
        null=True,
        blank=True)

    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='products')

    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    short_description = models.CharField(max_length=300, null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f"{self.title}({self.price})"
