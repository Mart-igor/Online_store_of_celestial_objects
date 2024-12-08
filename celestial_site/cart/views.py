from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from main.models import Celestial
from .forms import CartAddCelestialForm


@require_POST
def cart_add(request, celestial_obj_id):
    cart = Cart(request)
    celestial_obj = get_object_or_404(Celestial, id=celestial_obj_id)
    form = CartAddCelestialForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(celestial_obj=celestial_obj,
                 quantity=cd['quantity'],
                 override=cd['override'])
    return redirect('cart:cart_detail')
    

@require_POST
def cart_remove(request, celestial_obj_id):
    cart = Cart(request)
    celestial_obj = get_object_or_404(Celestial, id=celestial_obj_id)
    cart.remove(celestial_obj)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', context={'cart': cart})