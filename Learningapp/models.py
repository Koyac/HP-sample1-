from django.db import models

# Create your models here.
#データベースの作成
class HPModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')
    good = models.IntegerField(null=True,blank=True,default=0)
    read = models.IntegerField(null=True,blank=True,default=0)
    readtext = models.CharField(max_length=200,null=True,blank=True)