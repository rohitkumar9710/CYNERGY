from django.db import models

# Create your models here.
class Serviceinfo(models.Model):
    service_id = models.AutoField
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 200)
    phone_no = models.IntegerField()
    password = models.CharField(max_length=150)
    sign_up_date = models.DateField()
    city = models.CharField(max_length = 100,default = "")
    state = models.CharField(max_length = 50, default = "")
    addres = models.CharField(max_length=200,default = "")
    activestate = models.CharField(max_length =20, default="active")
    primary_work = models.CharField(max_length =50)
    secondary_work = models.CharField(max_length =50,default="")
    
    def __str__(self):
        return self.email  