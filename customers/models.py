from django.db import models

class Customer(models.Model):
    # Personal details
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    
    # Employment details
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.FloatField()

    def __str__(self):
        return self.name
