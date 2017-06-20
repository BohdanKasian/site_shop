from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



class Base (models.Model):
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE)
	# comments = models.TextField()
	link_to_image = models.CharField(max_length=25000)
	update = models.DateTimeField(auto_now=True, auto_now_add=False)
	create = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title


class Product (Base):
	title = models.CharField(
		max_length=250)
	product_name = models.CharField(
		max_length=200)
	description = models.TextField(
        blank=True,
        default="",)
	processor = models.CharField(
		max_length=200)
	video_card = models.CharField(
		max_length=200)
	color = models.CharField(
		max_length=200)
	resolution = models.CharField(
		max_length=200)
	price = models.DecimalField(
		max_digits=8,
        decimal_places=2,
        null=True,
        default=0.00,)
	weight = models.CharField(
		max_length=10)

	def __str__(self):
		return self.title

