from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('courier', 'Courier'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='admin')

class Parcel(models.Model):
    ROLE_CHOICES = (
        ('pending', 'Pending'),
        ('in_transit', 'In_Transit'),
        ('delivered', 'Delivered'),
    )

    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=12, choices=ROLE_CHOICES, default='pending')
    sender = models.ForeignKey(CustomUser, related_name='sent_parcels', on_delete=models.CASCADE)
    receiver = models.CharField(max_length=200)
    receiver_adress = models.TextField()
    courier = models.ForeignKey(CustomUser, related_name='courier_parcels', on_delete=models.CASCADE)
    creted_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField()

        
class DeliveryProof(models.Model):
    parcel = models.OneToOneField(Parcel, related_name='delivery_proof', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='delivery_proof/')
    timestamp = models.DateTimeField(auto_now_add=True)