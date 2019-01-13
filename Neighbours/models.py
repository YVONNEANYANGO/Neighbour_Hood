from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_lenth = 150)
    location = models.CharField(max_length = 150)
    occupants_count = models.CharField(max_length = 150)


    # methods 

    def create_neighbourhood(self):
        self.create()

    def delete_neighbourhood(self):
        self.delete()

    def update_neighbourhood(self):
        self.update()

    def __str__(self):
        return self.location

    @classmethod
    def get_neighbourhood(cls, neighbourhood_id):
        neighbourhood = Neighbourhood.objects.filter(name__location__icontains=neighbourhood_id)
        return neighbourhood


    class User(models.Model):
        username = models.CharField(max_length = 150)
        id = models.PrimaryKey(User, null=True, blank=True, on_delete=models.CASCADE)
        Neighbourhood = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
        email address = models.CharField(max_length = 150)

    