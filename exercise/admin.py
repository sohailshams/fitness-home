from django.contrib import admin
from .models import ExercisePlans

# Register your models here.


class ExercisePlanAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'timing',
        'access',
        'free_offer',
        'accompanied_guest',
        'price',

    )

    ordering = ('price',)


admin.site.register(ExercisePlans, ExercisePlanAdmin)
