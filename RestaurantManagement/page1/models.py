from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Role(models.Model):
    role_id=models.IntegerField(primary_key=True)
    role_name=models.CharField(max_length=20)
    status=models.BooleanField(default=True)
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
    cid=models.IntegerField(primary_key=True,auto_created=True,)
    cname=models.CharField(max_length=50,null=False,blank=False)
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.cname
    
class Subcategory(models.Model):
    cid=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    scname=models.CharField( max_length=200,null=False,blank=False)
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.scname

    
class Menutbl(models.Model):
    cid=models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    sub_category=models.ForeignKey(Subcategory,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=False,blank=False)
    description=models.CharField(max_length=200,null=False,blank=False)
    image = models.ImageField(upload_to="images", null=False, blank=False)
    price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Table_Details(models.Model):
    t_no=models.IntegerField(null=False,blank=False)
    capacity=models.IntegerField(null=False,blank=False)
    status=models.BooleanField(default=True)
    def __int__(self):
        return self.t_no


class Order(models.Model):
    customer_id=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    table_id=models.ForeignKey(Table_Details,null=True,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    price=models.FloatField(null=False,blank=False,default=0)
    status=models.BooleanField(default=False)
    old=models.BooleanField(default=False)
    ready_to_deliver=models.BooleanField(default=False)
    delivered=models.BooleanField(default=False)
    paid_status=models.BooleanField(default=False)

    def __int__(self):
        return self.customer_id.username

class Cart(models.Model):
    customer_id=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    table_id=models.ForeignKey(Table_Details,null=True,on_delete=models.CASCADE)
    order_id=models.ForeignKey(Order,null=True,on_delete=models.CASCADE)
    item=models.ForeignKey(Menutbl,null=True,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField(null=False,blank=False,default=0)
    price=models.FloatField(null=False,blank=False,default=0)
    status=models.BooleanField(default=True)
    incart=models.BooleanField(default=False)
    ordered=models.BooleanField(default=False)
    prepared=models.BooleanField(default=False)
    ready_to_deliver=models.BooleanField(default=False)
    delivered=models.BooleanField(default=False)
    paid=models.BooleanField(default=False)
    def __int__(self):
        return self.customer_id.username



# class Cart(models.Model):
#     order_id=models.ForeignKey('Order',null=True,on_delete=models.CASCADE)
#     t_id=models.ForeignKey(Table_Details,null=True,on_delete=models.CASCADE)
#     c_id=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
#     item_id=models.ForeignKey(Menutbl,null=True,on_delete=models.CASCADE)
#     date=models.DateTimeField(auto_now_add=True)
#     quantity=models.IntegerField(null=False,blank=False,default=1)
#     price=models.FloatField(null=False,blank=False)
#     status=models.BooleanField(default=True)


# class Order(models.Model):
#     c_id=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
#     t_id=models.ForeignKey(Table_Details,null=True,on_delete=models.CASCADE)
#     items=models.ManyToManyField(Menutbl,through='Cart')
#     o_date=models.DateTimeField(auto_now_add=True)
#     price=models.FloatField(null=False,blank=False,default=0.0)
#     status=models.BooleanField(default=False)

#     def __str__(self):
#         return f"Cart for {self.c_id.username}"



    



# # class Order(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     # items = models.ManyToManyField('Menutbl',through='Cart')
# #     order_date = models.DateTimeField(auto_now_add=True)
# #     total_amount = models.FloatField(default=0.0)
# #     t_id=models.ForeignKey(Table_Details,null=True,on_delete=models.CASCADE)
# #     status = models.BooleanField(default=True)
    

# #     def __str__(self):
# #         return f"Order #{self.id} - {self.user.username}"

