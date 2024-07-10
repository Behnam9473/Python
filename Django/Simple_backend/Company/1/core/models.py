# core/models.py

from django.db import models

class HomePage(models.Model):
    title = models.CharField(max_length=255)
    main_text = models.TextField()
    featured_image = models.ImageField(upload_to='home_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Carousel(models.Model):
    title = models.CharField(max_length=255)
    image_1 = models.ImageField(upload_to='carousel_images/')
    image_2 = models.ImageField(upload_to='carousel_images/')
    image_3 = models.ImageField(upload_to='carousel_images/')
    image_4 = models.ImageField(upload_to='carousel_images/')
    image_5 = models.ImageField(upload_to='carousel_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    history = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    team_photo = models.ImageField(upload_to='team_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    map_embed_code = models.TextField(blank=True, null=True)  # برای تعبیه نقشه گوگل
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

