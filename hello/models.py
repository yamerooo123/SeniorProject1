from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images', default='default_user_icon.jpg')
    birthdate = models.DateField()
    phoneno = models.CharField(max_length=10)
    address = models.TextField(max_length=255, null=True, blank=True)
    address1 = models.TextField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username




class ShoeFeatures(models.Model):
    product_id = models.IntegerField(primary_key=True)
    type1 = models.CharField(max_length=255)
    type2 = models.CharField(max_length=255)
    maincolor = models.CharField(max_length=255)
    subcolor = models.CharField(max_length=255)
    subcolor2 = models.CharField(max_length=255)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255)
    productImage = models.URLField(max_length=200)
    description = models.CharField(max_length=255)
    productName = models.CharField(max_length=255)
    InStock = models.IntegerField()