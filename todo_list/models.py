from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    user_input=models.TextField(max_length=200)
    Date=models.DateField()
    time1=models.TimeField()


    def __str__(self) -> str:
        return self.user_input