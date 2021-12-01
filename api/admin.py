from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('id','company_name','contact_no','profile_pic','address','availability','category')

@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = ('id','location','lab_name','contact_info','charges','test_name','testing_at')

@admin.register(Insuarance)
class CompanyRegisterAdmin(admin.ModelAdmin):
    list_display = ('id','company_name','company_code','contact_no','email','address')