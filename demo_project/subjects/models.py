from django.db import models

class Lectures(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()


class Subjects(models.Model):
    Subjects_name = models.CharField(max_length=20)
    Subjects_credit= models.IntegerField()
    lecture = models.ForeignKey(Lectures,on_delete=models.CASCADE)