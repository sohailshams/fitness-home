from django.db import models

# Create your models here.


class NutritionPlans(models.Model):

    class Meta:
        verbose_name_plural = 'Nutrition Plans'

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=80)
    purpose = models.CharField(max_length=120)
    meal_plan = models.CharField(max_length=120)
    grocery_list = models.CharField(max_length=120)
    message = models.CharField(max_length=120)
    coaching = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    product_type = models.CharField(max_length=254, default='nutrition_plan')

    def __str__(self):
        return self.name

