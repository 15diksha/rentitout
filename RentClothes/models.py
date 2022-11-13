from django.db import models
from Clothes.models import Clothes
from CustomerHome.models import Customer
from Owner.models import Owner


# Create your models here.
class RentClothes(models.Model):
    RentClothes_id = models.AutoField
    RentClothes_Date_of_Booking = models.DateField(blank=True,null=True)
    RentClothes_Date_of_Return = models.DateField(blank=True,null=True)
    Total_days = models.IntegerField()
    Advance_amount = models.IntegerField(blank=True,null=True)
    RentClothes_Total_amount = models.IntegerField(blank=True,null=True)
    isAvailable = models.BooleanField(default=True)
    isBillPaid = models.BooleanField(default=False)
    
    customer_email = models.CharField(max_length=100)
    request_responded_by = models.CharField(max_length=100,blank=True,null=True)
    request_status = models.CharField(max_length=30,default="Pending")

    # def __str__(self):
    #     return self.customer_email + ": " + str(self.Clothes_license_plate)