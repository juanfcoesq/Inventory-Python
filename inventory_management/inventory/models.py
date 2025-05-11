from email.policy import default

from django.db import models
from django.contrib.auth.models import User


class InventoryItem(models.Model):
	CATEGORY_CHOICES = [
		('electronics', 'Electronics'),
		('clothing', 'Clothing'),
		('furniture', 'Furniture'),
		('food', 'Food'),
	]

	name = models.CharField(max_length=200)
	quantity = models.IntegerField()
	category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	provider = models.CharField(max_length=200, default='Unknown')

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name
