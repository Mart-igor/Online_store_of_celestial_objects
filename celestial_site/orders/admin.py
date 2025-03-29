from django.contrib import admin
from .models import Order, OrderItems
from django.utils.safestring import mark_safe


class OrderItemInline(admin.TabularInline):
    model = OrderItems
    raw_id_fields = ['celestial_obj']


def order_stripe_payment(obj):
    url = obj.get_stripe_url()
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return ''

order_stripe_payment.short_description = 'Stripe payment'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    fields = ['id', 'first_name', 'last_name', 'email', 'adress', 'postal_code', 'city', 'paid',
              order_stripe_payment, 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
