
#from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator  # For phone number validation
from django.db import models

class Shop(models.Model):
    shopname = models.CharField(max_length=50,default="shop")  # Renamed from shopname
    city = models.CharField(max_length=16,default="iran")
    location = models.TextField(max_length=200)
    shopPhoneNumber = models.CharField(max_length=15, validators=[RegexValidator(regex=r'\d{10,14}', message='Enter a valid phone number')],default="09123456789")
    image = models.ImageField(upload_to='shop_images/', null=True, blank=True)  # Optional image
    class Meta:
        verbose_name = "فروشگاه"
    
    def __str__(self):
     return " {} /  {}".format(self.shopname,self.city)


class User(models.Model): 
    name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50) 
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(regex=r'\d{10,14}', message='Enter a valid phone number')],default="09123456789")
    national_code = models.CharField(max_length=10, null=True, blank=True)  # Optional national code
    email_address = models.EmailField(unique=True,null=True,blank=True)  # Use EmailField 
    # Remove password field and use Django's password hashing mechanisms
    # Consider using a CharField with limited options or a custom model for gender
    gender = models.CharField(max_length=10, null=True, blank=True)
    #start = 1
    #end = 2
    #cancel = 3
    #status_choices = (
    #(start, "زن"),                      بجای gender
    #(end, "مرد"),
    #(cancel, "ترجیح میدهم نگویم"),
    #status = models.IntegerField(choices=status_choices)
    age = models.PositiveIntegerField(null=True, blank=True)  # Allow null/blank for optional age
    class Meta:
        verbose_name = "کاربر" 

class Makeup(models.Model):
    shopname = models.ForeignKey(Shop,on_delete=models.CASCADE,default="shop")
    productname = models.CharField(max_length=20)
    remained = models.CharField(max_length=3)
    price = models.DecimalField(decimal_places=3,max_digits=10)
    maincategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    aboutproduct = models.TextField(max_length=350)
    expdate = models.DateField()
    class Meta:
        verbose_name = "لوازم آرایشی"

    def __str__(self):
     return " {} /  {} ".format(self.productname,self.shopname)


class Skincare(models.Model): 
    shopname =models.ForeignKey(Shop,on_delete=models.CASCADE,default="shop")
    productname = models.CharField(max_length=20)
    remained = models.CharField(max_length=3)
    price = models.DecimalField(decimal_places=3,max_digits=10)
    maincategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    aboutproduct = models.TextField(max_length=350)
    expdate = models.DateField()
    class Meta:  
        verbose_name = "لوازم مراقبت پوستی" 

    def __str__(self):
     return " {} /  {} ".format(self.productname,self.shopname)
 
    

class Digitalstuff(models.Model):
    shopname =models.ForeignKey(Shop,on_delete=models.CASCADE,default="shop")
    productname = models.CharField(max_length=20)
    remained = models.CharField(max_length=3)
    price = models.DecimalField(decimal_places=3,max_digits=10)
    maincategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    aboutproduct = models.TextField(max_length=350)
    manufacturing_country = models.CharField(max_length=20)
    warranty = models.IntegerField()
    class Meta:
        verbose_name = "لوازم برقی"

    def __str__(self):
      return " {} /  {} ".format(self.productname,self.shopname)
    

class Sell(models.Model):
    address = models.CharField(max_length=350)
    housenumber = models.IntegerField()
    postalcode = models.IntegerField()
    paymentmethod = models.CharField(max_length=1000)   # باید براش یه فیلد با دو سه تا انتخاب طراحی بشه
    sendingtime = models.CharField(max_length=1000)    #باید براش تایم پیشنهادی طراحی بشه
    receivername = models.CharField(max_length=25)
    class Meta:
        verbose_name = "فروش"


#class Shop(models.Model):
 #   class Meta:
 #       verbose_name = "فروشگاه" 
 #   shopname = models.CharField(max_length=50)
 #   location = models.TextField(max_length=200)
 #   shopphonenumber = models.CharField(max_length=11)
 #   image = models.ImageField(null=True)
       

#class User(models.Model):
 #   class Meta:
 #       verbose_name = "کاربر"
 #   name = models.CharField(max_length=12)
 #   lastname = models.CharField(max_length=12)
 #   userphonenumber = models.CharField(max_length=11)
 #   nationalcode = models.CharField(null=True,max_length=10)
 #   gmail = models.CharField(max_length=100)
 #   address = models.TextField(max_length=200)
 #   password = models.CharField(max_length=50)
 #   gender = models.BooleanField(null=True)
 #   age = models.DateField()

class  Comment(models.Model): 
    name = models.CharField(max_length=20) 
    commenttext = models.TextField(max_length=250) 
    shopname =models.ForeignKey(Shop,on_delete=models.CASCADE,default="shop")



   

