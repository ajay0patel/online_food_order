from django.db import models

# Create your models here.
class PizzaModel(models.Model):
	name = models.CharField(max_length=10)
	price = models.CharField(max_length=10)

	def __str__(self) -> str:
		return self.name

class CustomerModel(models.Model):
	userid = models.CharField(max_length=10)
	phonno = models.CharField(max_length=10)

class OrderModel(models.Model):
	username = models.CharField(max_length=10)
	phonno = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	ordereditems = models.CharField(max_length=500)
	status = models.CharField(max_length=10)
	totalAmount = models.IntegerField()
	created_date = models.DateTimeField()

	def __str__(self) -> str:
		return self.username

# class PizzaCategory(models.Model):