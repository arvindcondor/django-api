from django.db import models


class MyModel(models.Model):
    postId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()


