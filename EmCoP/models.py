from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Slider(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="Default description")
    img = models.ImageField(upload_to='slider/',)
    def __str__(self):
        return self.title


class Team(models.Model):
    position = models.CharField(max_length= 50)
    name = models.CharField(max_length= 100)
    image = models.ImageField(upload_to ='teams/')
    twitter_url = models.CharField(max_length=60, blank = True)
    instagram_url = models.CharField(max_length=78, blank=True)
    facebook_url = models.CharField(max_length=78,blank=True)
    linkedin_url = models.CharField(max_length=78, blank=True)


def __str__(self):
    return self.name


class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    image = models.ImageField(upload_to ='board/', blank=False)
    twitter_url = models.CharField(max_length=60, blank = True)
    linkedin_url = models.CharField(max_length=78, blank=True)

def __str__(self):
    return self.description


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class ContactMessage(models.Model):
    URGENCY_CHOICES = [
        ('low', 'Low Priority'),
        ('medium', 'Medium Priority'),
        ('high', 'High Priority'),
        ('emergency', 'Emergency')
    ]

    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed')
    ]

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES, default='low')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    
    # Location fields (optional)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    
    # Timestamp fields
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject} ({self.urgency})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

from django.core.validators import RegexValidator

class EmergencyAlert(models.Model):
    EMERGENCY_TYPES = [
        ('medical', 'Medical Emergency'),
        ('accident', 'Accident'),
        ('fire', 'Fire'),
        ('other', 'Other')
    ]

    phone_validator = RegexValidator(
        message="Enter a valid phone number."
    )

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=20,
        validators=[phone_validator]
    )
    location = models.CharField(max_length=255)
    emergency_type = models.CharField(
        max_length=20,
        choices=EMERGENCY_TYPES
    )
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.emergency_type} Emergency"