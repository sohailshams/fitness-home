import uuid

from django.db.models import Sum
from django.db import models

from django_countries.fields import CountryField


from merchandise.models import Product
from exercise.models import ExercisePlans
from nutrition.models import NutritionPlans
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update total each time a line item is added
        """
        product_total = self.productlineitem_set.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        exercise_total = self.exerciselineitem_set.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        nutrition_total = self.nutritionlineitem_set.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.order_total = product_total + exercise_total + nutrition_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    class Meta:
        abstract = True

    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'NAME {self.product.name} on order {self.order.order_number}'


class ProductLineItem(OrderLineItem):
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE
                                )


class ExerciseLineItem(OrderLineItem):
    product = models.ForeignKey(ExercisePlans, null=False, blank=False,
                                on_delete=models.CASCADE
                                )


class NutritionLineItem(OrderLineItem):
    product = models.ForeignKey(NutritionPlans, null=False, blank=False,
                                on_delete=models.CASCADE
                                )


