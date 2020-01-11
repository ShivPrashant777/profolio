from django.db import models

# Create your models here.
class UserAccount(models.Model):
    username = models.CharField(default='noname', max_length=50)
    password = models.CharField(max_length=10)
