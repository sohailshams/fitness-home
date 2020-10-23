from django.contrib import admin
from review.models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    To display the below fields to the Review admin panel.
    """
    list_display = (
        'user',

    )


admin.site.register(Review, ReviewAdmin)
