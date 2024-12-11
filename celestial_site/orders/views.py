from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItems
from django.urls import reverse


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST, request=request)
        if form.is_valid():
            order = form.save()
            for item in cart:
                discounted_price = item['celestial_obj'].sell_price()
                OrderItems.objects.create(order=order,
                                          celestial_obj=item['celestial_obj'],
                                          price=discounted_price,
                                          quantity=item['quantity'])
                cart.claer()
                request.session['order_id'] = order.id
                return redirect(reverse('payment:process'))

    else:
        form = OrderForm()
        return render(request, 'orders/create.html', context={'cart':cart, 'form': form})