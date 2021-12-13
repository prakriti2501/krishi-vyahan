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


