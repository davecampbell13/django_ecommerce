from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=400)
	price = models.IntegerField()

	def __str__(self):
		# returns blog title as print str
		return self.name

class Order(models.Model):
	user = models.ForeignKey(User)
	items = models.ManyToManyField(Item)
	status = models.IntegerField()
	