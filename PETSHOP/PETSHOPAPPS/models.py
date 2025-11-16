from django.db import models

# Create your models here.
class register(models.Model):
    firstname=models.CharField(max_length=50)
    secondname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    role=models.CharField(max_length=10)

class loggin(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=10)

class givee(models.Model): 
    name=models.CharField(max_length=25)   
    breed=models.CharField(max_length=25)
    age=models.CharField(max_length=25)
    colour=models.CharField(max_length=25)
    number=models.CharField(max_length=25)
    city=models.CharField(max_length=25)
    district=models.CharField(max_length=25)
    price=models.CharField(max_length=25)
    image=models.ImageField(default='0')

    
   



class adoptcuss(models.Model):
    customername=models.CharField(max_length=25)
    address=models.CharField(max_length=25)
    phone=models.CharField(max_length=11)

class vacc(models.Model):    
    vaccinedate=models.DateField(max_length=20)

class contactt(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    subject=models.CharField(max_length=11)
    message=models.CharField(max_length=11)

class dewo(models.Model):    
    dewormdate=models.DateField(max_length=20)


