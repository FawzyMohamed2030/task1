from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name
