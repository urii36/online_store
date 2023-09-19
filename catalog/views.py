from django.shortcuts import render

from catalog.models import Product


def home_page(request):
    products = Product.objects.all()
    context = {
        'title': 'SkyStore',
        'products': products
    }
    return render(request, 'catalog/home_page.html', context)


def contacts(request):
    context = {
        'title': 'Contacts',
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) {message}')
    return render(request, "catalog/contacts.html", context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_detail.html', context)
