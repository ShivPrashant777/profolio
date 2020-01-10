from django.db import models

# Create your models here.
class User_accounts(models.Model):
    name: models.CharField(max_length=50)
    password: models.CharField(max_length=10)
