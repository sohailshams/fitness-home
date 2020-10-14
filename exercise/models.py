from django.db import models

# Create your models here.


class ExercisePlans(models.Model):

    class Meta:
        verbose_name_plural = 'Exercise Plans'

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=80)
    timing = models.CharField(max_length=120)
    access = models.CharField(max_length=254)
    free_offer = models.CharField(max_length=500)
    accompanied_guest = models.CharField(max_length=220)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    product_type = models.CharField(max_length=254, default='exercise_plan')

    def __str__(self):
        return self.name
