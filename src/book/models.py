from django.conf import settings
from django.db import models

# Create your models here.


class Book(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL)
	name 		= models.CharField(max_length=120)
	author 		= models.CharField(max_length=120)
	pages 		= models.IntegerField()
	ratings 	= models.DecimalField(max_digits=5,decimal_places=2)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name