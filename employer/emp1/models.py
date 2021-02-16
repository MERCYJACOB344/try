from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    tittle=models.TextField(null=True,blank=True)
    status=models.CharField(default='inactive',max_length=10)
    created=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
# Create your models here.
