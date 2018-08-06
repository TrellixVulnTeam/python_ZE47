from django.db import models
#创建出版社库
class Publisher(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)

    def __str__(self):
        return self.name

# Create your models here.
#创建用户库
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=32,unique=True)
    password=models.CharField(max_length=32)
    def __str__(self):
        return self.username

