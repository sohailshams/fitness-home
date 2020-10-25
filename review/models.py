from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True,
                             related_name="reviews")
    your_review = models.TextField(max_length=1500, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username