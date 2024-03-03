from django.db import models
from django.db.models import CharField, TextField, BooleanField, IntegerField

class Data(models.Model):
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.text
