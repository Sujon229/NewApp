from django.db import models

# Create your models here.
class Product(models.Model):
    title  = models.CharField(max_length=50)
    describe = models.CharField(max_length=150)
    price = models.CharField(max_length=4)
    def __str__(self):
        return self.title
    
class User(models.Model):
    fname  = models.CharField(max_length=50)
    lname = models.CharField(max_length=150)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.fname + " " + self.lname
    
