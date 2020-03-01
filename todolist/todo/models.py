from django.db import models
from django.urls import reverse

class Todo(models.Model):
        entry = models.CharField(max_length=500)
        pub_date = models.DateTimeField(auto_now=True)
        