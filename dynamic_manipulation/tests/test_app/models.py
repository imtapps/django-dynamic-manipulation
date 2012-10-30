from django.db import models


class Sample(models.Model):
    first_field = models.CharField(max_length=10)
    second_field = models.CharField(max_length=10)
