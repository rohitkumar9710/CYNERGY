from django.db import models


# Create your models here.
class Custinfo(models.Model):
    cust_id = models.AutoField
    cust_name = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 200,default = "")
    phone_no = models.IntegerField()
    password = models.CharField(max_length=150)
    sign_up_date = models.DateField()
    city = models.CharField(max_length = 100,default = "")
    state = models.CharField(max_length = 50, default = "")
    addres = models.CharField(max_length=200,default = "")
    loginstate = models.CharField(max_length = 10,default= "no")
    gender = models.CharField( max_length=50,default = "Other")
    image = models.ImageField( upload_to='customer/images', default = "")

    def __str__(self):
        return self.email  


class Contact(models.Model):
    id = models.AutoField
    name = models.CharField( max_length=150)
    email = models.EmailField( max_length=254,default="")
    subject = models.CharField( max_length=200,default = "")
    comment = models.CharField(max_length=2000)
    date = models.DateField()

    def __str__(self):
        return self.email


class Custom_order(models.Model):
    customer_email = models.CharField(max_length = 150)
    serviceman_email = models.CharField( max_length=150)
    accept_status = models.CharField( max_length=50, default= "None")
    work_done_status = models.CharField( default= "None", max_length=50)
    feedback = models.CharField(default = "None", max_length=50)
    request_date = models.DateField()
    deadline_date = models.DateField(null=True, blank=True)
    accept_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    work_description = models.CharField(default = "None", max_length=50)
    
    def __str__(self):
        return self.customer_email


class Customer_random(models.Model):
    customer_email = models.CharField(max_length = 150)
    serviceman_email = models.CharField( max_length=150,default="none")
    accept_status = models.CharField( max_length=50, default= "None")
    work_done_status = models.CharField( default= "None", max_length=50)
    feedback = models.CharField(default = "None", max_length=50)
    request_date = models.DateField()
    deadline_date = models.DateField()
    accept_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    work_address = models.CharField(max_length = 500,default="")
    work_description = models.CharField(default = "None", max_length=50)

    def __str__(self):
        return self.customer_email