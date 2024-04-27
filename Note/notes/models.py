from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    descrption = models.TextField()
    user = models.ForeignKey(User,related_name="notes",on_delete=models.CASCADE)