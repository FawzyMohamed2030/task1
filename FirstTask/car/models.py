from django.db import models
from client.models import Client #connect models togeather
from company.models import Company


class Car(models.Model): #create model for each app
    model = models.CharField(max_length=50)
    model_age = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    sold_by = models.ManyToManyField(Client) #for manytomany
    manufacture = models.ForeignKey(Company, on_delete=models.CASCADE) #for one to many

    def __str__(self):
        return self.model