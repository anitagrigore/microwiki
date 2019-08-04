from django.db import models


class Pages(models.Model):
    title = models.CharField(max_length=64)
    preview = models.CharField(max_length=255, default=" ")
    content = models.TextField()

