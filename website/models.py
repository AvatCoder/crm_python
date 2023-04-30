from django.db import models

# Create your models here.
class Record(models.Model):
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now=True)
    first_name = models.CharField('First Name',max_length=50)
    last_name = models.CharField('Last Name',max_length=50)
    email = models.CharField('Email Address',max_length=50)
    phone = models.CharField('Phone Number',max_length=14)
    state = models.CharField('State',max_length=50)
    city = models.CharField('City',max_length=50)
    address = models.CharField('Address',max_length=50)
    zip_code = models.CharField('Zip-Code',max_length=50)
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    
