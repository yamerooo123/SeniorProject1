from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone





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
    class Meta:
        verbose_name = "Profile Management"
        verbose_name_plural = "Profile Management"


class ShoeFeatures(models.Model):
    product_id = models.BigIntegerField(primary_key=True, unique=True)
    type1 = models.CharField(max_length=255)
    type2 = models.CharField(max_length=255)
    maincolor = models.CharField(max_length=255, default="Black")
    subcolor = models.CharField(max_length=255, default="Black")
    subcolor2 = models.CharField(max_length=255, default="Black")
    size = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255, verbose_name="Brand")
    productImage = models.URLField(max_length=200)
    description = models.CharField(max_length=255)
    short_description = models.CharField(max_length=100)
    productName = models.CharField(max_length=255, verbose_name="Model", unique=True)
    InStock = models.IntegerField(verbose_name="In stock")
    product_idName = models.CharField(max_length=255, verbose_name="Product ID")
    material = models.CharField(max_length=255,  verbose_name="Material")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    class Meta:
        verbose_name = "Men product "
        verbose_name_plural = "Men products"
        
    def __str__(self):
        return f"{self.product_idName} {self.productName}"

class Wishlist(models.Model):
    username = models.CharField(max_length=255)
    productName = models.CharField(max_length=255)
    price = models.IntegerField()
    available_quantity = models.IntegerField()
    productImage = models.URLField(max_length=255)
    type2 = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, verbose_name="Brand")
    material = models.CharField(max_length=255, verbose_name="Material")
    product_id = models.BigIntegerField()
    
    def __str__(self):
        return f"Wishlist for {self.username} - Product ID: {self.product_id}"

class WomenShoeFeatures(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    type1 = models.CharField(max_length=255)
    type2 = models.CharField(max_length=255)
    maincolor = models.CharField(max_length=255, default="Black")
    subcolor = models.CharField(max_length=255, default="Black")
    subcolor2 = models.CharField(max_length=255, default="Black")
    size = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255, verbose_name="Brand")
    productImage = models.URLField(max_length=200)
    description = models.CharField(max_length=255)
    short_description = models.CharField(max_length=100)
    productName = models.CharField(max_length=255, verbose_name="Model", unique=True)
    InStock = models.IntegerField(verbose_name="In stock")
    product_idName = models.CharField(max_length=255, verbose_name="Product ID")
    material = models.CharField(max_length=255,  verbose_name="Material")
    class Meta:
        verbose_name = "Women product"
        verbose_name_plural = "Women products"
    
    def __str__(self):
        return f"{self.product_idName} {self.productName}"

class M_Cart(models.Model):
    product_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    productName = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.PositiveIntegerField(default=1)
    product_image = models.URLField(max_length=255)
    main_color = models.CharField(max_length=255)
    sub_color = models.CharField(max_length=255)
    product_size = models.IntegerField()
    InStock = models.IntegerField()

    def __str__(self):
        return str(self.productName)
    
class W_Cart(models.Model):
    product_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    productName = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.PositiveIntegerField(default=1)
    product_image = models.URLField(max_length=255)
    main_color = models.CharField(max_length=255)
    sub_color = models.CharField(max_length=255)
    product_size = models.IntegerField()

    def __str__(self):
        return str(self.productName)
    
class OrderTransaction(models.Model):
    STATUS_CHOICES = (
        ('Ongoing', 'Ongoing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )
    PAYMENT_CHOICES = (
        ('CreditCard', 'CreditCard'),
        ('CashOnDelivery','CashOnDelivery'),
        ('Cancelled','Cancelled'),
    )
    class Meta:
        verbose_name = "Sales Management"
        verbose_name_plural = "Sales Management"

    product_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    productName = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.PositiveIntegerField(default=1)
    product_image = models.URLField(max_length=255)
    main_color = models.CharField(max_length=255,  default="Black")
    sub_color = models.CharField(max_length=255, default="Black")
    product_size = models.IntegerField()
    payment_method = models.CharField(max_length=255, choices=PAYMENT_CHOICES)
    created_by = models.DateTimeField(default=timezone.now, verbose_name="Order date")
    delivery_status = models.CharField(max_length=255, default="Ongoing", choices=STATUS_CHOICES)
    total_amount_vat = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name="Total amount")




    
    






