from django.conf import settings
from main.models import Celestial
from decimal import Decimal

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):
        return sum( item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        total = sum((Decimal(item['price']) - (Decimal(item['price']) \
            * Decimal(item['celestial_obj'].discount / 100))) * item['quantity']
                for item in self.cart.values())
        return format(total, '.2f')
    
    def remove(self, celestial_obj):
        celestial_obj_id = str(celestial_obj.id)
        if celestial_obj_id in self.cart:
            del self.cart[celestial_obj_id]
            self.save()

    def add(self, celestial_obj, quantity, override=False):
        celestial_obj_id = str(celestial_obj.id)
        if celestial_obj_id not in self.cart:
            self.cart[celestial_obj_id] = {'quantity': 0,
                                           'price': str(celestial_obj.price)}
        if override:
            self.cart[celestial_obj_id]['quantity'] = quantity
        else:
            self.cart[celestial_obj_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
       del self.session[settings.CART_SESSION_ID]


    def __iter__(self):
        celestial_objs_ids = self.cart.keys()
        celestial_objs = Celestial.objects.filter(id__in=celestial_objs_ids)
        cart = self.cart.copy()
        for celestial_obj in celestial_objs:
            cart[str(celestial_obj.id)]['celestial_obj'] = celestial_obj
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
