from django.db import models

# Create your models here.
class WorldConf(models.Model):
    domain = models.CharField('Domain', max_length=200)
    add_time = models.DateTimeField('Add Time', auto_now_add=True)

