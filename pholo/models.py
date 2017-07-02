from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)

    def __str__(self):
		return "Store: " + self.name


class Table(models.Model):
	number = models.CharField(max_length=30)
	status = models.CharField(max_length=30)
	store = models.ForeignKey(Store, default=1)

	def __str__(self):
		return 'Table: ' + self.number


class Booking(models.Model):
	table = models.ForeignKey(Table, default=None)
	user = models.ForeignKey(User, default=None)
	active = models.BooleanField(default=True)


class Product(models.Model):
	name = models.CharField(max_length=128)


class Request(models.Model):
	booking = models.ForeignKey(Booking, default=None)
	product = models.ForeignKey(Product, default=None)



admin.site.register(Store)
admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(Product)
admin.site.register(Request)