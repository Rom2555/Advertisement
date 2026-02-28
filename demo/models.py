from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, CASCADE, CharField


# Create your models here.
class Advertisement(models.Model):
    user = ForeignKey(User, on_delete=CASCADE)
    text = CharField()
