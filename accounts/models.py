from django.db import models

# Create your models here.
class vocab(models.Model):
    vocab_name = models.CharField(max_length=100,null=True,blank=True)
    vocab_detail = models.CharField(max_length=200,null=True,blank=True)
