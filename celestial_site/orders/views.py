from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItems
from django.urls import reverse


# def create_order(request):
#     cart = Cart(request)
#     if request.method == 'POST':
#         form = OrderForm(request.POST, request=request)
#         if form.is_valid():
#             order = form.save(commit=False)  # Не сохраняем еще
#             order.user = request.user  # Если вы хотите связать заказ с текущим пользователем
#             order.save()  # Теперь сохраняем заказ
#             for item in cart:
#                 discounted_price = item['celestial_obj'].cell_price()
#                 OrderItems.objects.create(order=order,
#                                           celestial_obj=item['celestial_obj'],
#                                           price=discounted_price,
#                                           quantity=item['quantity'])
#             cart.clear()
#             request.session['order_id'] = order.id
#             return redirect(reverse('payment:process'))
#         else:
#             # Если форма не валидна, отображаем ошибки
#             return render(request, 'orders/create.html', context={'cart': cart, 'form': form})

#     else:
#         form = OrderForm()
#         return render(request, 'orders/create.html', context={'cart':cart, 'form': form})
    


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST, request=request)
        if form.is_valid():
            order = form.save()  # Сохраняем заказ
            
            for item in cart:
                celestial_obj = item['celestial_obj']
                if celestial_obj is not None:  # Проверяем, что celestial_obj существует
                    discounted_price = celestial_obj.cell_price()
                    try:
                        OrderItems.objects.create(
                            order=order,
                            celestial_obj=celestial_obj,
                            price=discounted_price,
                            quantity=item['quantity']
                        )
                    except Exception as e:
                        # Логируем или обрабатываем ошибку
                        print(f"Error creating OrderItems: {e}")
                        # Можно добавить логику для обработки ошибки, например, вернуть сообщение об ошибке

            cart.clear()  # Очищаем корзину после завершения создания всех элементов заказа
            
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
        else:
            # Если форма не валидна, отображаем ошибки
            return render(request, 'orders/create.html', context={'cart': cart, 'form': form})

    else:
        form = OrderForm()
        return render(request, 'orders/create.html', context={'cart': cart, 'form': form})