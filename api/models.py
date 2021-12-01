from django.db import models

# Create your models here.
class Transport(models.Model):
    category_options = (
        ('CROP','CROP'),
        ('MACHINERY','MACHINERY'),
        ('PRODUCT','PRODUCT')
    )
    company_name = models.CharField(max_length =50)
    contact_no = models.CharField(max_length =10)
    profile_pic =  models.ImageField(upload_to='transport/profile_image/',default='default.ico')
    address = models.CharField(max_length =50)
    availability = models.CharField(max_length =50)
    category = models.CharField(
        max_length=10, choices=category_options, default="CROP")

class Lab(models.Model):
    lab_options = (
        ('PLACE','PLACE'),
        ('LAB', 'LAB'),
    )
    location = models.CharField(max_length =50)
    lab_name = models.CharField(max_length =50)
    contact_info = models.CharField(max_length =10)
    charges = models.IntegerField()
    test_name = models.CharField(max_length =50)
    testing_at = models.CharField(
        max_length=10, choices=lab_options, default="LAB")

class Insuarance(models.Model):
    company_name = models.CharField(max_length =50)
    company_code = models.CharField(max_length =50)
    contact_no = models.CharField(max_length =50)
    email = models.EmailField(max_length =50)
    address = models.CharField(max_length =50)


