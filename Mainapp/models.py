from django.db import models
import datetime
from django.contrib.auth.models import User,auth
from django import forms
# Create your models here.

class Catagory(models.Model):

    garment_choices=( 
    ("Mens", "Mens"), 
    ("Womens", "Womens"), 
    ("Kids", "Kids"),
    ("Other", "Other"), 
    )

    name    =   models.CharField(max_length = 50)

    garment_type = models.CharField(max_length = 50 , blank = True,  choices = garment_choices)
    

    def __str__(self):
        return self.name


class Product(models.Model) :

    name        =   models.TextField(max_length = 200)

    catagory    =   models.ForeignKey(Catagory,null = True , on_delete = models.CASCADE)

    tag         =   models.TextField(blank = True ,max_length = 200)   

    price       =   models.IntegerField(null = False)

    false_price = models.IntegerField(null = True)

    cod_available     =   models.BooleanField()
    
    emi         =   models.TextField(max_length = 100)

    offer       =   models.TextField(blank = True)

    return_policy = models.TextField(max_length = 50)

    discription   = models.TextField(max_length = 500)

    image_1     = models.ImageField(upload_to='products',default='default.jpg',) 

    image_2     = models.ImageField(upload_to='products',default='default.jpg',) 

    image_3     = models.ImageField(upload_to='products',default='default.jpg',) 

    def __str__(self):
        return self.name


class Cart(models.Model) :

    product     = models.ForeignKey(Product , on_delete = models.CASCADE)

    user        = models.ForeignKey(User , on_delete = models.CASCADE)

    quantity    = models.IntegerField()


class Order(models.Model) :

    product     = models.ForeignKey(Product , null=True, blank=True, on_delete = models.SET_NULL)

    custmer     = models.ForeignKey(User , null=True, blank=True, on_delete = models.SET_NULL)

    # paid_amount

    date_time   = models.DateTimeField(auto_now_add=True, blank=True)

    payment_done = models.BooleanField()

    delivery_done = models.BooleanField()

    # delivery_status =

    # payment_method = 

class User_detail(models.Model) :

    address_types=( 
    ("Office", "Office"), 
    ("Home", "Home"), 
    ("Commercial", "Commercial"), 
    )

    user        = models.ForeignKey(User , on_delete = models.CASCADE)

    full_name   = models.TextField(null = False , max_length = 150)

    phone       = models.IntegerField( max_length = 10 ,null = False )

    alt_phone   = models.IntegerField( max_length = 10, null = True )

    landmark    = models.TextField(null = False , max_length = 150)

    town        = models.TextField(null = False , max_length = 50)

    pincode       = models.IntegerField( max_length = 10 ,null = True )

    address_type = models.CharField(max_length = 50 , blank = True,  choices = address_types)
    
     

