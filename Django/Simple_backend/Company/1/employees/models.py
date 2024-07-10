# person/models.py
from django.db import models
from companies.models import Companies

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photos/')
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
