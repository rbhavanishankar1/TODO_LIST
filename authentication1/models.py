from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class register_model(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    gender=models.CharField(max_length=15,choices=[['Male','Male'],['Female','Female']])
    phone=models.BigIntegerField()

def __str__(self) -> str:
        return self.user
    
# class Meta:
#     ordering = ['user']

# from django.db import models
# from django.contrib.auth.models import User

# class register_model(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="User")
#     gender = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female')], verbose_name="Gender")
#     phone = models.CharField(max_length=15, verbose_name="Phone Number")

#     class Meta:
#         verbose_name = "Registration"
#         verbose_name_plural = "Registrations"