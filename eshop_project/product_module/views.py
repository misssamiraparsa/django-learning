from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Avg


# Create your views here.

def product_list(request):
    products = Product.objects.all().order_by('-price')
    number_of_products = products.count()
    avg_rating = products.aggregate(Avg("rating"))

    return render(request, 'product_module/product_list.html', {
        'products': products,
        'total_number_of_products':number_of_products,
        'average_ratings':avg_rating

    })


def product_detail(request, slug):
    #product = Product.objects.get(id=product_id)
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_module/product_detail.html', {
        'product': product
    })
