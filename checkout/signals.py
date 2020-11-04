from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ProductLineItem, ExerciseLineItem, NutritionLineItem

# Chris Zielinski suggested to write three @receiver


@receiver(post_save, sender=ProductLineItem)
@receiver(post_save, sender=ExerciseLineItem)
@receiver(post_save, sender=NutritionLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=ProductLineItem)
@receiver(post_delete, sender=ExerciseLineItem)
@receiver(post_delete, sender=NutritionLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
