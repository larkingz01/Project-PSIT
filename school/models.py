from django.db import models
import time
# Create your models here.
class Time(models.Model):
 	"""docstring for ClassName"""
 	name1 = models.CharField(max_length=200)
 	name2 = models.CharField(max_length=200)
 	name3 = models.CharField(max_length=200)
 	name4 = models.CharField(max_length=200)
 	court = models.CharField(max_length=100)
 	time = models.CharField(max_length=100)
 	
 	def __str__(self):
 		return '{} {} {}'.format(self.name1, self.court, self.time)

# Create your models here.