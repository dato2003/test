from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=39)
    characters = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    
