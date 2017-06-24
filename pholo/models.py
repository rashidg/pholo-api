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
