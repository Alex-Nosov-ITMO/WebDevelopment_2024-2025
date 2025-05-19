from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"


class Product(models.Model):
    SIZES = [
        ('XXS', 'Double Extra Small'),
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    ]

    COLORS = [
        ('red', 'Red'),
        ('white', 'White'),
        ('black', 'Black'),
        ('grey', 'Grey'),   
    ]


    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=3, choices=SIZES, default='M')
    color = models.CharField(max_length=10, choices=COLORS, default='white')
    image = models.ImageField(upload_to='cars/')
    category = models.CharField(max_length=10, choices=[('t', 'T-shirt'), ('h', 'Hoodies')], default='t-s')

    def __str__(self):
        return self.name

