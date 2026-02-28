from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Advertisement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True,)
    opened = models.BooleanField(default=True)
