from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from django.templatetags.static import static
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    Images = models.ImageField(null = True, blank= True, upload_to= 'images')
    
    def __str__(self):
        return self.name.upper()
    
    
class Products(models.Model):
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    Name = models.CharField(max_length = 50)
    Model = models.CharField(max_length = 50)
    Price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0, null=True, blank=True)
    description = models.TextField(max_length=1000, blank=True, default=None, null = True)
    Images = models.ImageField(null = True, blank= True, upload_to= 'images')

    def __str__(self):
        return self.Name.upper()
    
    @property
    def offer_price(self):
        return self.Price - (self.Price * self.discount / 100)
    
    
class UserProfile(models.Model):
    Gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    pro = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    profile = models.ImageField(upload_to="static/profile", max_length=100, default=static("images/profileimage.png"), null=True, blank=True)
    gender = models.CharField(choices=Gender_choices, max_length=6, default=None, null=True, blank=True)
    mobile = PhoneNumberField(null=False, blank=False, default='+91')

    def __str__(self):
        return str(self.pro.username)
    
    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(pro=instance)
        else:
            instance.userprofile.save()
