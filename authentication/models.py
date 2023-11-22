from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class register_model(models.Model):

    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    gender=models.CharField(max_length=20,choices=[['Male','Male'],['Female','Female']])
    phone=models.BigIntegerField()

