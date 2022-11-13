from django.db import models

# Create your models here.
class Clothes(models.Model):
    Clothes_ID = models.AutoField
    Clothes_name = models.CharField(max_length=60)
    Clothes_brand = models.CharField(max_length=60)
    
    Clothes_type = models.CharField(max_length=20)
    
    Clothes_size = models.CharField(max_length=5)
    Clothes_color = models.CharField(max_length=20)
    
    Clothes_uploaded_by = models.CharField(max_length=100)
    Clothes_image1 = models.ImageField(upload_to='img/Clothes_images/')
    Clothes_image2 = models.ImageField(upload_to='img/Clothes_images/')
    Clothes_image3 = models.ImageField(upload_to='img/Clothes_images/')
   
    Clothes_description = models.CharField(max_length=1500)
    Clothes_price = models.IntegerField()

    # def __str__(self):
    #     return self.Clothes_license_plate + " : " + str(self.Clothes_name)