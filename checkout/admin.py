from django.contrib import admin
from .models import Order, ProductLineItem, ExerciseLineItem, NutritionLineItem


"""
Inline admin class ProductLineItemAdminInline
"""


class ProductLineItemAdminInline(admin.TabularInline):
    model = ProductLineItem
    readonly_fields = ('lineitem_total',)


"""
Inline admin class ExerciseLineItemAdminInline
"""


class ExerciseLineItemAdminInline(admin.TabularInline):
    model = ExerciseLineItem
    readonly_fields = ('lineitem_total',)


"""
Inline admin class NutritionLineItemAdminInline
"""


class NutritionLineItemAdminInline(admin.TabularInline):
    model = NutritionLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):

    """
    This inline item allow us to add and edit line items in the admin
    right from inside the order model.
    """
    inlines = (ProductLineItemAdminInline, ExerciseLineItemAdminInline,
               NutritionLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                       'order_total')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'order_total',)

    list_display = ('order_number', 'date', 'full_name', 'order_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
admin.site.register(ProductLineItem)
admin.site.register(ExerciseLineItem)
admin.site.register(NutritionLineItem)


