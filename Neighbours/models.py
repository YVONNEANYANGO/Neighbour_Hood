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
    user_email_address = models.CharField(max_length = 150)

    
class Business(models.Model):
    business_id = models.PrimaryKey
    business_name = models.CharField(max_length =150)
    User = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Neighbourhood = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    business_email_address = models.CharField(max_length =150)

    def __str__(self):
        return self.business_name
    
    def create_business(self):
        self.create()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()

    @classmethod
    def search_by_business_name(cls,search_term):
        business = cls.objects.filter(business_name__icontains=search_term)
        return business



    