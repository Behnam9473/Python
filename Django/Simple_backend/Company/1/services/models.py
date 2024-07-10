from django.db import models
from companies.models import Companies

class Services(models.Model):
    name = models.CharField(max_length=450)
    description = models.TextField(max_length=1500)
    photo = models.ImageField(upload_to='photos/')
    company = models.ManyToManyField(Companies,  related_name='portfolio')

    def __str__(self) -> str:
        return self.name
    
    