from django.db import models

class Companies(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1500)
    photo = models.ImageField(upload_to='photos/')

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.name