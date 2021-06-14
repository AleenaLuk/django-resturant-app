from django.db import models

class Resturant(models.Model):
    name = models.CharField(max_length=225)
    price = models.CharField(max_length=225)
    image = models.CharField(max_length=225)

    def __str__(self):
        return self.name
