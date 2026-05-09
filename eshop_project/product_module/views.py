from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DeleteView

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

    # def get_queryset(self):
    #   base_query = super(ProductDetailView, self).get_queryset()
    #  data = base_query.filter(is_active=True)
    # return data


class ProductDetailView(DeleteView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get("product_favorite")
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        return context


class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = Product.objects.get(pk=product_id)
        request.session["product_favorite"] = product_id
        return redirect(product.get_absolute_url())
