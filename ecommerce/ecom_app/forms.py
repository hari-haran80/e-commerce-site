from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'
        
class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
        
class t_shirtForm(forms.ModelForm):
    class Meta:
        model = T_shirt
        fields = '__all__'
        
class HeadPhoneForm(forms.ModelForm):
    class Meta:
        model = Head_phone
        fields = '__all__'