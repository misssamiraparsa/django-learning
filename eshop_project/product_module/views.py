from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .models import Product, ProductCategory
from django.db.models import Avg


# Create your views here.

class ProductListView(TemplateView):
    template_name = 'product_module/product_list.html'

    def get_context_data(self, **kwargs):
        products = Product.objects.all().order_by('-price')[:5]
        context = super(ProductListView, self).get_context_data()
        context['products'] = products
        return context


class ProductDetailView(ListView):
    template_name = 'product_module/product_detail.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        base_query = super(ProductDetailView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_module/product_detail.html', {
        'product': product
    })
