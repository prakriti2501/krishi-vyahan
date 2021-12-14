from django.db import models

# Create your models here.
class Transport(models.Model):
    category_options = (
        ('CROP','CROP'),
        ('MACHINERY','MACHINERY'),
        ('PRODUCT','PRODUCT')
    )
    company_name = models.CharField(max_length =50,null = True, blank=True)
    contact_no = models.CharField(max_length =10,null = True, blank=True)
    profile_pic =  models.ImageField(upload_to='transport/profile_image/',default='default.ico',null = True, blank=True)
    address = models.CharField(max_length =50,null = True, blank=True)
    availability = models.CharField(max_length =50,null = True, blank=True)
    category = models.CharField(
        max_length=10, choices=category_options, default="CROP",null = True, blank=True)

class Lab(models.Model):
    lab_options = (
        ('PLACE','PLACE'),
        ('LAB', 'LAB'),
    )
    location = models.CharField(max_length =50,null = True, blank=True)
    lab_name = models.CharField(max_length =50,null = True, blank=True)
    contact_info = models.CharField(max_length =10,null = True, blank=True)
    charges = models.IntegerField(null = True, blank=True)
    test_name = models.CharField(max_length =500,null = True, blank=True)
    testing_at = models.CharField(
        max_length=10, choices=lab_options, default="LAB",null = True, blank=True)

class Insuarance(models.Model):
    company_name = models.CharField(max_length =50,null = True, blank=True)
    company_code = models.CharField(max_length =50,null = True, blank=True)
    contact_no = models.CharField(max_length =50,null = True, blank=True)
    email = models.EmailField(max_length =50,null = True, blank=True)
    address = models.CharField(max_length =50,null = True, blank=True)

class Seller(models.Model):
    seller_name = models.CharField(max_length =255,null = True, blank=True)
    quantity =  models.IntegerField()
    price = models.CharField(max_length =50,null = True, blank=True)
    district = models.CharField(max_length =50,null = True, blank=True)
    pincode = models.CharField(max_length =50,null = True, blank=True)
    contact = models.CharField(max_length =50,null = True, blank=True)
    profile_pic = models.ImageField(upload_to='seller/profile_image/',default='default.ico',null = True, blank=True)
    country = models.CharField(max_length =50,null = True, blank=True)
    price_with_transportation = models.CharField(max_length =50,null = True, blank=True)

class Shop(models.Model):
    item_name = models.CharField(max_length =50,null = True, blank=True)
    price = models.CharField(max_length =50,null = True, blank=True)
    quantity = models.CharField(max_length =50,null = True, blank=True)
    item_pic = models.ImageField(upload_to='shop/profile_image/',default='default.ico',null = True, blank=True)


