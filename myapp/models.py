from django.db import models


# Create your models here.
class Item(models.Model):
	title = models.CharField(max_length=100)
	picture = models.ImageField(upload_to='items/pictures/')
	height = models.DecimalField(max_digits=8, decimal_places=2)
	width = models.DecimalField(max_digits=8, decimal_places=2)
	manufacturingcountry = models.CharField(max_length=50)
	description =  models.CharField(max_length=300)
	price = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.title

	def delete(self, *args, **kwargs):
		self.picture.delete()
		super().delete(*args, **kwargs)

