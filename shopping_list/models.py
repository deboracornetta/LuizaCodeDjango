from django.db import models
from django.contrib.auth.models import User

class Shopping_List(models.Model):
    complete = models.BooleanField(default=False)
    item = models.CharField(max_length=100)


    def __str__(self):
        return self.item