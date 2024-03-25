from django.db import models

class Event(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)

