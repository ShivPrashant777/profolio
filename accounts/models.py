from django.db import models

def user_dir_path(instance, filename):
    print(instance.username,filename)
    return 'user_{0}/{1}'.format(instance.username, filename)


class UserAccount(models.Model):
    username = models.CharField(default='noname', max_length=50)
    password = models.CharField(max_length=10)
    file_user = models.FileField(upload_to = user_dir_path, default= 'null')