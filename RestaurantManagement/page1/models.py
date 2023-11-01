from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Role(models.Model):
    role_id=models.IntegerField(primary_key=True)
    role_name=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.role_name

class Person(models.Model):
    user_id=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=15)
    email=models.EmailField(max_length=25)
    phone=models.CharField(max_length=12)
    role_id=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=200,blank=True,null=True)
    password=models.CharField(max_length=20)
    status=models.BooleanField(null=True,blank=True,default=True)

    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=50,null=False,blank=False)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.cname
    
class Menutbl(models.Model):
    cid=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=False,blank=False)
    description=models.CharField(max_length=70,null=False,blank=False)
    image=models.ImageField(upload_to="images",null=False,blank=False)
    price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    



