from django.db import models


class Laptop(models.Model):
    LaptopName = models.CharField(max_length = 50)
    Model = models.CharField(max_length = 50)
    Price = models.IntegerField()
    Images = models.ImageField(null = True, blank= True, upload_to= 'images')

    def __str__(self):
        return self.LaptopName.upper()
    
class Mobile(models.Model):
    MobileName = models.CharField(max_length = 50)
    Model = models.CharField(max_length = 50)
    Price = models.IntegerField()
    Images = models.ImageField(null = True, blank= True, upload_to= 'images')

    def __str__(self):
        return self.MobileName.upper()
    
class T_shirt(models.Model):
    t_shirt = models.CharField(max_length = 50)
    Color = models.CharField(max_length = 50)
    Price = models.IntegerField()
    Images = models.ImageField(null = True, blank= True, upload_to= 'images')

    def __str__(self):
        return self.t_shirt.upper()
    
class Head_phone(models.Model):
    HeadphoneName = models.CharField(max_length = 50)
    Model = models.CharField(max_length = 50)
    Price = models.IntegerField()
    Images = models.ImageField(null = True, blank= True, upload_to= 'images')

    def __str__(self):
        return self.HeadphoneName.upper()