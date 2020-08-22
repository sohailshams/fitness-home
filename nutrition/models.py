from django.db import models

# Create your models here.


class NutritionPlans(models.Model):

    class Meta:
        verbose_name_plural = 'Nutrition Plans'

    name = models.CharField(max_length=80)
    purpose = models.CharField(max_length=120)
    meal_plan = models.CharField(max_length=120)
    grocery_list = models.CharField(max_length=120)
    message = models.CharField(max_length=120)
    coaching = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
