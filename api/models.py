from django.db import models


class MyModel(models.Model):
    userId = models.IntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()


