from django.db import models
 
class cars(models.Model):
    car=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    horse_power= models.IntegerField()

