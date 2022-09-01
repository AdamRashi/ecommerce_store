from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from store.models import Product
from .shopping_cart import ShoppingCart


def cart_summary(request):
    cart = ShoppingCart(request)
    return render(request, 'store/cart/summary.html', {'cart': cart})


def cart_add(request):
    cart = ShoppingCart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)

        cart_qty = len(cart)
        response = JsonResponse({'qty': cart_qty})
        return response
