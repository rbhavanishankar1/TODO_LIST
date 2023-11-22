from django.db import models

# Create your models here.

class todo(models.Model):
    
    user_input=models.TextField(max_length=200)
    Date=models.DateField()
    time1=models.TimeField()


