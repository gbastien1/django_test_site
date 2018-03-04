from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=300)
	description = models.TextField(default="")
	slug = models.SlugField(unique=True)
	
	@models.permalink
	def get_absolute_url(self):
		return 'catalog:category', (self.slug)
	
	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=300)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	date_created = models.DateTimeField('date of creation')
	slug = models.SlugField(unique=True)

	@models.permalink
	def get_absolute_url(self):
		return 'catalog:product', (self.slug)

	def __str__(self):
		return self.name
