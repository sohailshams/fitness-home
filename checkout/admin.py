from django.contrib import admin
from .models import Order, OrderLineItem


"""
Inline admin class OrderLineItemAdminInline
"""


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('product_lineitem_total', 'exercise_lineitem_total',
                       'nutrition_lineitem_total',)


class OrderAdmin(admin.ModelAdmin):

    """
    This inline item allow us to add and edit line items in the admin
    right from inside the order model.
    """
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                       'order_total')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'order_total',)

    list_display = ('order_number', 'date', 'full_name', 'order_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

